import pygame.font

class BUtton:
    def __init__(self,ai_game,msg) -> None:
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width,self.height = 200,50
        self.button_color = (0,135,0)
        self.text_color =(255,255,255)
        self.font = pygame.font.SysFont(None,48)    #指定用什么字体来渲染文本 None是使用默认字体,48是字号

        # Pygame 处理文本的方式是，将要显示的字符串渲染为图像。最后，调用 _prep_msg() 来处理这样的渲染

        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)         # msg 是要在按钮中显示的文本
    
    def _prep_msg(self,msg):
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        # font.render()会将文本转化成图像,其中接受一个布尔值,表示是否开启反锯齿功能
        #后面两个是文本颜色和背景颜色  (若果没有设置背景颜色,pygame会使用透明的背景)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        self.screen.fill(self.button_color,self.rect)           #调用 screen.fill() 来绘制表示按钮的矩形
        self.screen.blit(self.msg_image,self.msg_image_rect)       
        # 调用screen.blit() 来向它传递一幅图像以及与该图像相关联的rect，从而在屏幕上绘制文本图像。