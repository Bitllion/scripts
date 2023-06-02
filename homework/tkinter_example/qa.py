# -*- encoding: utf-8 -*-
"""
@文件        :qa.py
@说明        :
@时间        :2022/06/08 01:17:54
@作者        :TM_FULLNAME
@版本        :1.0
"""
# 导入tkinter模块
from tkinter import *
from tkinter import messagebox


from index import IndexWindow

# 导入json模块
import json

# 导入配置类
from settings import config


class QaWindow(object):
    def __init__(self):
        # 创建self.gui窗口
        self.gui = Tk()

        # 设置self.gui窗口的大小
        self.gui.geometry("800x450")

        # 设置标题
        self.gui.title("知识问答")

        # 设置logo
        self.gui.iconbitmap(config.icon_path)
        # 初始化问题的标数
        self.q_no = 0

        # 为display_question函数指定ques，以便稍后更新。
        self.display_title()
        self.display_question()

        # 设置答案选项
        self.opt_selected = IntVar()

        # 设置答案选项
        self.opts = self.radio_buttons()

        # 显示当前问题的选项
        self.display_options()

        # 显示“下一步”和“退出”按钮。
        self.buttons()

        # 问题数量
        self.data_size = len(question)

        # 保留正确答案的计数器
        self.correct = 0

        # self.gui.mainloop

    """
    此方法用于显示结果,它统计正确答案和错误答案的数量然后在末尾显示为消息框
    """

    def display_result(self):
        # 计算错误的计数
        wrong_count = self.data_size - self.correct
        correct = f"正确数量: {self.correct}"
        wrong = f"错误数量: {wrong_count}"

        # 计算正确答案的百分比
        score = int(self.correct / self.data_size * 100)
        result = f"答题正确百分比: {score}%"

        # 显示消息框以显示结果
        messagebox.showinfo("结果", f"{result}\n{correct}\n{wrong}")

        self.exit_gui()

    # 此方法在单击“下一步”后检查答案。
    def check_ans(self, q_no):

        # 检查所选选项是否正确
        if self.opt_selected.get() == answer[q_no]:
            return True

    """
    此方法用于通过调用检查答案和问题编号来检查当前问题的答案。如果问题正确，则将计数增加1，然后将问题编号增加1。如果是lastquestion，则调用display result以显示消息框。否则显示下一个问题。
    """

    def next_btn(self):

        # 检查答案是否正确
        if self.check_ans(self.q_no):
            # 如果答案正确，则将正确值增加1
            self.correct += 1

        # 通过递增q_no 计数器转到下一个问题
        self.q_no += 1

        # 检查q_no size是否等于数据大小
        if self.q_no == self.data_size:
            # 如果正确，则显示分数
            self.display_result()
            self.gui.destroy()
        else:
            # 显示下一个问题
            self.display_question()
            self.display_options()

    def buttons(self):

        # 第一个按钮是移动到下一个问题
        next_button = Button(
            self.gui,
            text="下一题",
            command=self.next_btn,
            width=10,
            bg="pink",
            fg="white",
            font=("ariel", 16, "bold"),
        )

        # 将按钮放置在屏幕上
        next_button.place(x=350, y=380)

        # 这是用于退出self.gui的第二个按钮
        quit_button = Button(
            self.gui,
            text="退出",
            command=self.exit_gui,
            width=10,
            height=2,
            font=("ariel", 16, " bold"),
        )

        # 在屏幕上放置退出按钮
        quit_button.place(x=600, y=180)

    def exit_gui(self):
        self.gui.destroy()
        IndexWindow()

    """
    此方法取消选择屏幕上的单选按钮，然后用于显示当前问题的可用选项，我们通过问题编号获得这些选项，并更新单选按钮中当前问题的每个选项。
    """

    def display_options(self):
        val = 0

        # 取消选择选项
        self.opt_selected.set(0)

        # 循环显示单选按钮文本的选项。
        for option in options[self.q_no]:
            self.opts[val]["text"] = option
            val += 1

    # 此方法在屏幕上显示当前问题
    def display_question(self):

        # 设置问题属性
        q_no = Label(
            self.gui,
            text=question[self.q_no],
            width=60,
            font=("ariel", 16, "bold"),
            anchor="w",
        )

        # 将选项置于屏幕上
        q_no.place(x=70, y=100)

    # 此方法用于显示标题
    def display_title(self):

        # 要显示的标题
        title = Label(
            self.gui,
            text="党的历史知识在线问答系统",
            width=50,
            bg="red",
            fg="yellow",
            font=("ariel", 20, "bold"),
        )

        title.place(x=0, y=2)

    """
    This method shows the radio buttons to select the Question on the screen at the specified position. It also returns a list of radio button which are later used to add the options to them.
    """

    def radio_buttons(self):

        # 使用空选项列表初始化列表
        q_list = []

        # 第一个选项的位置
        y_pos = 150

        # 将选项添加到列表中
        while len(q_list) < 4:

            # 设置单选按钮属性
            radio_btn = Radiobutton(
                self.gui,
                text=" ",
                variable=self.opt_selected,
                value=len(q_list) + 1,
                font=("ariel", 14),
            )

            # 将按钮添加到列表
            q_list.append(radio_btn)

            # 放置按钮
            radio_btn.place(x=100, y=y_pos)

            # 将y轴位置增加40
            y_pos += 40

        # 返回单选按钮
        return q_list


# 从json文件获取数据
with open(config.exam_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# 设置问题、选项和答案
question = data["question"]
options = data["options"]
answer = data["answer"]


if __name__ == "__main__":
    # 创建测验类的对象
    quiz = QaWindow()
    # 创建测验窗口
    quiz.gui.mainloop()
