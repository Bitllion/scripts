#!/bin/bash
#清理缓存包括日志、集群状态
rm -rf /var/log/slurm*
rm -rf /var/spool/slurm*
# ubuntu 安装slurm slurm-wlm
apt install -y slurm-wlm slurm
mkdir /var/log/slurm
# 判断系统语言是否为中文
if [[ $(locale | grep LANG=zh_CN) ]]; then
    # 获取系统信息
    SOCKET=$(lscpu | grep -E '座' | awk '{print $2}' | sed -n '2p')
    CORES=$(lscpu | grep -E '每个座的核数' | awk '{print $NF}')
    THREADS=$(lscpu | grep -E '每个核的线程数' | awk '{print $NF}')
    MEMORY=$(free -m | grep 内存 | awk '{print $2}')
else
    SOCKET=$(lscpu | grep -E '^Socket' | awk '{print $2}')
    CORES=$(lscpu | grep -E '^Core' | awk '{print $4}' | head -n 1)
    THREADS=$(lscpu | grep -E '^Thread' | awk '{print $4}' | head -n 1)
    MEMORY=$(free -m | grep Mem | awk '{print $2}')
fi
echo "Socket: $SOCKET , Cores: $CORES , Threads: $THREADS , Memory: $MEMORY MB"

# 获取hostname
HOSTNAME=$(hostname)

# 文本如下
echo "ClusterName=cool
ControlMachine=orange
SlurmUser=root
SlurmctldPort=6817
SlurmdPort=6818
AuthType=auth/munge
StateSaveLocation=/var/spool/slurmctld
SlurmdSpoolDir=/var/spool/slurmd
SwitchType=switch/none
MpiDefault=none
SlurmctldPidFile=/var/run/slurmctld.pid
SlurmdPidFile=/var/run/slurmd.pid
ProctrackType=proctrack/pgid
SelectType=select/cons_tres
SelectTypeParameters=CR_Core_Memory
ReturnToService=0
SlurmctldTimeout=300
SlurmdTimeout=300
InactiveLimit=0
MinJobAge=300
KillWait=30
Waittime=0
SlurmctldDebug=info
SlurmctldLogFile=/var/log/slurm/slurmctld.log
SlurmdDebug=info
SlurmdLogFile=/var/log/slurm/slurmd.log
JobCompType=jobcomp/none
" > slurm.conf
#只输入一个换行
echo "" >> slurm.conf
echo  "ControlMachine=$HOSTNAME" >> slurm.conf
echo "" >> slurm.conf
echo "NodeName=$HOSTNAME RealMemory=$MEMORY Sockets=$SOCKET CoresPerSocket=$CORES ThreadsPerCore=$THREADS State=UNKNOWN" >> slurm.conf
echo "" >> slurm.conf
echo "PartitionName=compute Nodes=$HOSTNAME Default=YES MaxTime=INFINITE State=UP" >> slurm.conf

mv slurm.conf /etc/slurm/slurm.conf

systemctl enable slurmctld --now
systemctl enable slurmd --now