from kivy.app import App
from kivy.uix.button import Button

# 关联kv模板的处理类   
# 格式： 文件名+App  
# 系统会自动关联同一目录下的kv模板
class HelloApp(App):
    pass

# NButton组件的处理类 
# Button是父类（父组件）
class NButton(Button): 
    def onclick(self): # 组件相关的处理方法
        self.text = 'Hi boy!' # 改变NButton的text内容

# 运行app
HelloApp().run() 