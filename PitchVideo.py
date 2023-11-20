from manim import *
import numpy as np

fill_opacity_black_rectangle = 0.75
font_title = 36


sommaire_sketch = VGroup(*[Line([-4.5*(1-i/3)+4.5*i/3+0.2,0,0],[-4.5*(1-(i+1)/3)+4.5*(i+1)/3-0.2,0,0], stroke_width=5) for i in range(3)],\
                                 *[Circle(0.2, fill_opacity=0.5).move_to([-4.5*(1-i/3)+4.5*i/3,0,0]) for i in range(4)])
sommaire_text = VGroup(Text("Problem statement", font_size=18).move_to([-4.5,-0.5,0]),\
                        Text("Temporary solution", font_size=18).move_to([-1.5,-0.5,0]),\
                        Text("Quantum approach", font_size=18).move_to([1.5,-0.5,0]),\
                        Text("Project outlook", font_size=18).move_to([4.5,-0.5,0]))

def Bullet(self, txt, pos, e=0.2, r=0.04, font=24, duration=1):
    text = Text(txt, font_size=font)
    circle = Circle(r, fill_opacity=1, color=BLUE).move_to(pos)
    self.play(Create(circle), run_time = 0.4)
    self.play(Write(text.move_to(text.get_center()-text.get_left()-text.get_top()+pos+[e,0.15,0])), run_time=duration)
    return VGroup(text, circle)

def Bullet_add(self, txt, pos, e=0.2, r=0.04, font=24):
    text = Text(txt, font_size=font)
    circle = Circle(r, fill_opacity=1, color=BLUE).move_to(pos)
    self.add(circle)
    self.add(text.move_to(text.get_center()-text.get_left()-text.get_top()+pos+[e,0.15,0]))
    return VGroup(text, circle)

def rmv_all(self,obj, duration=0.25):
    self.play(AnimationGroup(*[FadeOut(obj[i], run_time=duration) for i in range(len(obj))]))


def slide_number(self,i):
    num = Text(str(i)+"/13", font_size=16).move_to([5.75,-3.5,0])
    self.add(num)
    return num



class Title(Scene):
    def construct(self):
        
        ##########
        self.wait(0.1)
        self.next_slide()


        r = 0.25
        e = 0.85
        circle1 = Circle(r, color=RED, fill_opacity=1).move_to([-1,0,0])
        circle2 = Circle(r, color=RED, fill_opacity=1).move_to([1,0,0])
        circle3 = Circle(r,color=GREY, fill_opacity=1).move_to([0,0,0])
        
        def func(t):
            if t>10:
                return 1/5
            elif t>5:
                return (t-10)/(5-10) + 1/5*(t-5)/(10-5)
            else:
                return 1
        
        t = ValueTracker(0)
        CO2 = VGroup(Line([1,r/3,0],[-1,r/3,0],color=WHITE),Line([1,-r/3,0],[-1,-r/3,0],color=WHITE),circle1,circle2,circle3)
        CO2_ = CO2.copy()
        CO2.add_updater(lambda x: x.become(CO2_)\
                        .move_to([np.sin(2*t.get_value())*func(t.get_value()), np.sin(1.4*t.get_value())*func(t.get_value()),0]).rotate(np.sin(t.get_value()))\
                       .scale(func(t.get_value())))
        self.add(CO2)
        
        hexa1 = RegularPolygon(6, color=GRAY)
        hexa2 = RegularPolygon(6, color=GRAY).move_to([0,np.sqrt(3),0])
        
        mof = VGroup(hexa1, hexa2, Line([-1/2*e,np.sqrt(3)/2*e,0],[1/2*e,np.sqrt(3)/2*e,0], color=GRAY),\
                    Line([-1*e, np.sqrt(3),0],[-1/2*e, np.sqrt(3)*(1+1/2*e),0], color=GRAY),\
                    Line([1*e, np.sqrt(3),0],[1/2*e, np.sqrt(3)*(1+1/2*e),0], color=GRAY),\
                    Line([-1/2, 3*np.sqrt(3)/2,0],[0,1/2+3*np.sqrt(3)/2,0], color=GRAY),\
                    Line([1/2, 3*np.sqrt(3)/2,0],[0,1/2+3*np.sqrt(3)/2,0], color=GRAY),\
                    Circle(r*0.75,color=RED, fill_opacity=1).move_to([0,1/2+3/2*np.sqrt(3),0]))

        mof1 = mof.copy().rotate(2*np.pi/3, about_point =[0,0,0])
        mof2 = mof.copy().rotate(-2*np.pi/3, about_point =[0,0,0])
        MOF = VGroup(mof,mof1,mof2)
        
        L = 3*np.sqrt(3)/2+1/2
        full = VGroup(MOF, \
                     MOF.copy().rotate(np.pi, about_point=[0,0,0]).shift([-np.sqrt(3)*L, -L, 0]),\
                     MOF.copy().rotate(np.pi, about_point=[0,0,0]).shift([np.sqrt(3)*L, -L, 0]),\
                     MOF.copy().shift([-np.sqrt(3)*L, -3*L, 0]))
        full = VGroup(*[MOF.copy().rotate(np.pi/3*i, about_point=[0,-2*L,0]) for i in range(6)])
        
        
        crystal = (VGroup(full, full.copy().shift([6*L*np.cos(5*np.pi/6),6*L*np.sin(5*np.pi/6),0])\
                       ,full.copy().shift([0,6*L,0])\
                       ,full.copy().shift([6*L*np.cos(np.pi/6),6*L*np.sin(np.pi/6),0])\
                       ,full.copy().shift([-6*L*np.cos(5*np.pi/6),-6*L*np.sin(5*np.pi/6),0])).scale(1/4).shift([8,8,0]))
        
        self.add(crystal)
        def ratefunc(t):
            return np.tanh(3*t)
        
        self.play(t.animate.set_value(12), run_time=4, rate_func=linear)
        self.play(crystal.animate.move_to([0.8,0.81,0]) ,t.animate.set_value(21), run_time=3, rate_func=linear)
        self.play(Flash(CO2, color=BLUE, line_length=0.25))
        self.wait(0.5)
        

        RR = Rectangle(height=10,width=20,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0)
        self.play(FadeIn(RR))

        
        Title1 = Text("MATERIAL CHARACTERISATION", font_size=40,weight=BOLD).move_to([0,1,0])
        Title2 = Text("FOR CO2 CAPTURE", font_size=40,weight=BOLD).move_to([0,0.5,0])
        Subtitle = Text("Presentation video", font_size=24).move_to([0,-0.5,0])
        Title = VGroup(Title1,Title2,Subtitle)
        name = Text("CuriousTurtles",color=BLUE, font_size=24).move_to([0,-1,0])


        self.play(FadeIn(Title))
        self.play(Write(name))
        self.wait(0.5)


        ##########
        self.next_slide()

        self.play(FadeOut(Title),run_time=0.75 )
        self.play(FadeOut(name),run_time=0.75 )
        # self.play(FadeOut(CO2_,CO2,crystal),run_time=0.75 )
        rmv_all(self,[CO2,crystal], 0)
        self.wait(0.5)
        rmv_all(self,[RR])

        
        # self.play(AnimationGroup(*[Create(sommaire_sketch[i]) for i in [3,0,4,1,5,2,6]], lag_ratio=0.5, run_time=2))
        # self.play(AnimationGroup(*[Write(sommaire_text[i]) for i in range(4)], lag_ratio=0.5))      
        # self.wait(1)

        # RR = Rectangle(height=4,width=10,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([2,0,0])
        # self.play(FadeIn(RR))
        # self.wait(1)

        # rmv_all(self,[sommaire_sketch,sommaire_text])
        # self.wait(0.5)


class Problem(Scene):
    def construct(self):


        Title = Text("Problem statement", font_size=font_title)
        self.add(Title.move_to([0,3.5,0]))

        sn = slide_number(self,1)

        nx = 15
        lx = 6
        ly = 4

        axes = Axes(
            x_range=[0, 1, 1/nx],
            y_range=[0, 1, 1/4],
            x_length=lx,
            y_length=ly,
            axis_config={"color": BLUE},
            x_axis_config={
                # "numbers_to_include": np.arange(1900, 2022, 1/nx),
                # "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )

        # self.add(axes)
        ticks = VGroup(Text("1900", font_size=18).move_to([-lx/2,-ly/2*1.15,0]),Text("2023", font_size=18).move_to([lx/2,-ly/2*1.15    ,0]),\
                      Text("0", font_size=18).move_to([-lx/2*1.05,-ly/2*0.98,0]), Text("35", font_size=18).move_to([-lx/2*1.1,ly/2,0]))
        Labels = VGroup(Text("CO2\n[Gt]", font_size=24).move_to([-lx/2*1.2,0,0]), Text("Year", font_size=24).move_to([0,-ly/2*1.15,0]))
        Plot = VGroup(axes, Labels, ticks)
        self.play(Create(axes))
        self.wait(1)
        self.play(Write(Labels))
        self.play(Write(ticks))

        h = 4/35873946500*np.array([2302604650.0,3104450150.0,3371523800.0,3845023200.0,3906025937.5,4868344512.5,6298916275.0,9026560875.0,12917584000.0,17822177250.0,19789989250.0,22792702375.0,25307740500.0,31481553875.0,35873946500.0])

        rectangles = VGroup(*[Rectangle(width=lx/nx, height=0).move_to([i/nx*lx-lx/2+lx/nx/2,-ly/2,0]) for i in range(nx)])
        # rectangles2 = VGroup(*[Rectangle(width=lx/nx, height=0.4*np.exp(2.5*i/nx)).move_to([i/nx*lx-lx/2+lx/nx/2,-ly/2+0.4*np.exp(2.5*i/nx)/2,0]) for i in range(nx)])
        rectangles2 = VGroup(*[Rectangle(width=lx/nx, height=h[i], color=BLUE, fill_opacity=0.25).move_to([i/nx*lx-lx/2+lx/nx/2,-ly/2+h[i]/2,0]) for i in range(nx)])
        # self.add(rectangles)
        self.wait(0.5)
        self.play(Transform(rectangles,rectangles2))
        self.wait(0.5)
        Graph = VGroup(Plot, rectangles)
        
        self.play(Graph.animate.shift([-3,0,0]))

        r = 0.04
        e = 0.2


        t1 = Bullet_add(self, "Exponential increase of CO2 emission", [0.6,2,0], e, r)
        t2 = Bullet_add(self, "Too profound changes are needed \nin many hard to abate sectors", [0.6,1,0], e, r)
        t3 = Bullet_add(self, "Mitigate the effect in the waiting \nof a sustainable solution", [0.6,0,0], e, r)
        self.wait(1)

        # rmv_all(self,[sn,Title,t1,t2,t3,Graph])
        # self.wait(1)


    
class TemporarySolution(Scene):
    def construct(self):
        config.disable_caching = True

        # self.add(sommaire_sketch)
        # self.add(sommaire_text)
        # self.wait(1)
        # RR1 = Rectangle(height=4,width=6,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([3,0,0])
        # RR2 = Rectangle(height=4,width=4,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([-5,0,0])
        # self.play(AnimationGroup(FadeIn(RR1),FadeIn(RR2)))
        # self.wait(1)
        # self.play(FadeOut(sommaire_sketch, run_time=0))
        # self.play(FadeOut(sommaire_text, run_time=0))
        # self.wait(0.5)
        # rmv_all(self, [RR1,RR2])

        r = 0.25
        e = 0.85
        
        hexa1 = RegularPolygon(6, color=GRAY)
        hexa2 = RegularPolygon(6, color=GRAY).move_to([0,np.sqrt(3),0])
        
        mof = VGroup(hexa1, hexa2, Line([-1/2*e,np.sqrt(3)/2*e,0],[1/2*e,np.sqrt(3)/2*e,0], color=GRAY),\
                    Line([-1*e, np.sqrt(3),0],[-1/2*e, np.sqrt(3)*(1+1/2*e),0], color=GRAY),\
                    Line([1*e, np.sqrt(3),0],[1/2*e, np.sqrt(3)*(1+1/2*e),0], color=GRAY),\
                    Line([-1/2, 3*np.sqrt(3)/2,0],[0,1/2+3*np.sqrt(3)/2,0], color=GRAY),\
                    Line([1/2, 3*np.sqrt(3)/2,0],[0,1/2+3*np.sqrt(3)/2,0], color=GRAY),\
                    Circle(r*0.75,color=RED, fill_opacity=1).move_to([0,1/2+3/2*np.sqrt(3),0]))

        mof1 = mof.copy().rotate(2*np.pi/3, about_point =[0,0,0])
        mof2 = mof.copy().rotate(-2*np.pi/3, about_point =[0,0,0])
        MOF = VGroup(mof,mof1,mof2)
        
        L = 3*np.sqrt(3)/2+1/2
        full = VGroup(MOF, \
                     MOF.copy().rotate(np.pi, about_point=[0,0,0]).shift([-np.sqrt(3)*L, -L, 0]),\
                     MOF.copy().rotate(np.pi, about_point=[0,0,0]).shift([np.sqrt(3)*L, -L, 0]),\
                     MOF.copy().shift([-np.sqrt(3)*L, -3*L, 0]))
        full = VGroup(*[MOF.copy().rotate(np.pi/3*i, about_point=[0,-2*L,0]) for i in range(6)])
        
        
        crystal = (VGroup(full, full.copy().shift([6*L*np.cos(5*np.pi/6),6*L*np.sin(5*np.pi/6),0])\
                       ,full.copy().shift([0,6*L,0])\
                       ,full.copy().shift([6*L*np.cos(np.pi/6),6*L*np.sin(np.pi/6),0])\
                       ,full.copy().shift([-6*L*np.cos(5*np.pi/6),-6*L*np.sin(5*np.pi/6),0])).scale(1/4).shift([8,8,0]))
        
        self.add(crystal.move_to([3,2,0]))
        self.add(Rectangle(width=20, height=10, fill_color=BLACK, stroke_width=0, fill_opacity=0.75))
        Title = Text("Temporary Solution", font_size=font_title).move_to([-3,3.5,0])
        self.add(Title)
        sn = slide_number(self,2)
        t1 = Bullet_add(self,"One way to slow dow the effect of the climate \nchange is to capture the carbon in the atmosphere", [-6,1.5,0])
        t2 = Bullet_add(self,"This can be done by nanoporous material such as \nMetallic Organic Framework (MOF)", [-6,0.5,0])
        t5 = Bullet_add(self,"Such solution would be rather straightfoward to set up", [-6,-0.5,0])
        t3 = Bullet_add(self,"Experimental tests on molecules can be costly and slow", [-6,-1.5,0])
        t4 = Bullet_add(self,"To find new good candidates, machine learning techniques have been used", [-6,-2.5,0])
        self.wait(1)


class ML(Scene):
    def construct(self):

        Title = Text("Prediction Model", font_size=font_title)
        self.add(Title.move_to([0,3.5,0]))
        sn = slide_number(self,3)

        def MLpoint(mol, val, L=1.5):
             return VGroup(mol,RoundedRectangle(corner_radius=0.25, height=L, width=L, color=RED),\
            RoundedRectangle(corner_radius=0.25, height=L, width=L, color=RED).set_opacity(0.25),\
            Text(val, font_size=16).move_to([-L*0.7/2,L*0.7/2,0]))

        def Gauge(theta=np.pi*0.5):
            n = 12
            c = Arc(radius = 0.4, angle=PI)
            R = Line([-0.4,0,0],[0.4,0,0])
            L = Line([0.1*np.cos(theta),0.1*np.sin(theta),0],[0.85*0.4*np.cos(theta),0.85*0.4*np.sin(theta),0],stroke_width=2.5)
            r = 0.3
            rr = 0.38
            lines = [Line([r*np.cos(np.pi*i/n),r*np.sin(np.pi*i/n),0],[rr*np.cos(np.pi*i/n),rr*np.sin(np.pi*i/n),0], stroke_width=1) for i in range(n)]
            return VGroup(c,R,*lines,L)

        a = 0.9
        ML = VGroup(Rectangle(height=3, width=3),\
        Gauge().move_to([a,a,0]),Gauge().move_to([-a,a,0])\
        ,Gauge().move_to([a,-a,0]),Gauge().move_to([-a,-a,0])).move_to([0,0.5,0])

        mol1 = VGroup(*[Circle(0.05, fill_opacity=1).move_to([0.3*np.cos(2*np.pi*i/6),0.3*np.sin(2*np.pi*i/6),0]) for i in range(6)],\
                      *[Line([0.3*np.cos(2*np.pi*i/6),0.3*np.sin(2*np.pi*i/6),0],\
                        [0.3*np.cos(2*np.pi*(i+1)/6),0.3*np.sin(2*np.pi*(i+1)/6),0],color=RED) for i in range(6)],\
                        Circle(0.05, fill_opacity=1).move_to([0.6*np.cos(2*np.pi*2/6),0.6*np.sin(2*np.pi*2/6),0]),\
                        Line([0.3*np.cos(2*np.pi*2/6),0.3*np.sin(2*np.pi*2/6),0],[0.6*np.cos(2*np.pi*2/6),0.6*np.sin(2*np.pi*2/6),0],color=RED))
        mol2 = VGroup(*[Circle(0.05, fill_opacity=1).move_to([0.3*np.cos(2*np.pi*i/5),0.3*np.sin(2*np.pi*i/5),0]) for i in range(5)],\
                      *[Line([0.3*np.cos(2*np.pi*i/5),0.3*np.sin(2*np.pi*i/5),0],\
                        [0.3*np.cos(2*np.pi*(i+1)/5),0.3*np.sin(2*np.pi*(i+1)/5),0],color=RED) for i in range(5)],\
                        Circle(0.05, fill_opacity=1).move_to([0.6*np.cos(2*np.pi*2/5),0.6*np.sin(2*np.pi*2/5),0]),\
                        Line([0.3*np.cos(2*np.pi*2/5),0.3*np.sin(2*np.pi*2/5),0],[0.6*np.cos(2*np.pi*2/5),0.6*np.sin(2*np.pi*2/5),0],color=RED),\
                        Circle(0.05, fill_opacity=1).move_to([0.6*np.cos(2*np.pi*4/5),0.6*np.sin(2*np.pi*4/5),0]),\
                        Line([0.3*np.cos(2*np.pi*4/5),0.3*np.sin(2*np.pi*4/5),0],[0.6*np.cos(2*np.pi*4/5),0.6*np.sin(2*np.pi*4/5),0],color=RED))
        mol3 = VGroup(*[Circle(0.05, fill_opacity=1).move_to([0.3*i,0,0]) for i in [-1,0,1]],\
                      Line([-0.3,0,0],[0,0,0],color=RED),Line([0.3,0,0],[0,0,0],color=RED),\
                        Circle(0.05,fill_opacity=1).move_to([0,0.3,0]), Line([0,0,0],[0,0.3,0], color=RED))
        
        mol9 = VGroup(*[Circle(0.05, fill_opacity=1).move_to([0.3*np.cos(2*np.pi*i/4),0.3*np.sin(2*np.pi*i/4),0]) for i in range(4)],\
                      *[Line([0.3*np.cos(2*np.pi*i/4),0.3*np.sin(2*np.pi*i/4),0],\
                        [0.3*np.cos(2*np.pi*(i+1)/4),0.3*np.sin(2*np.pi*(i+1)/4),0],color=RED) for i in range(4)],\
                        Circle(0.05, fill_opacity=1).move_to([0.6*np.cos(2*np.pi*2/4),0.6*np.sin(2*np.pi*2/4),0]),\
                        Line([0.3*np.cos(2*np.pi*2/4),0.3*np.sin(2*np.pi*2/4),0],[0.6*np.cos(2*np.pi*2/4),0.6*np.sin(2*np.pi*2/4),0],color=RED))

        mol_arr = [mol1,mol3,mol2,mol9]
        val_arr = ["2.4","0.2","3.0","1.1"]
        mols = VGroup(*[MLpoint(mol_arr[i], val_arr[i]).move_to([-4,3*(1-i/(len(val_arr)-1))-2*i/(len(val_arr)-1),0])\
                         for i in range(len(val_arr))])

        texts = [Text("Experimental data are used to train the model", font_size=24).move_to([0,-3,0]),\
                 Text("Carbon affinity of new molecules can be inferred", font_size=24).move_to([0,-3,0])]

        self.add(mols)
        self.add(ML)
        self.wait(0.1)

        ##########
        self.next_slide()

        self.add(texts[0])
        self.wait(0.5)
        self.play(AnimationGroup(*[FadeOut(mols[i],target_position=[0,0.5,0]) for i in range(len(mols))], lag_ratio = 0.1))
        self.wait(0.5)
        

        ML2 = VGroup(Rectangle(height=3, width=3),\
        Gauge(np.pi*0.1).move_to([a,a,0]),Gauge(np.pi*0.7).move_to([-a,a,0])\
        ,Gauge(np.pi*0.9).move_to([a,-a,0]),Gauge(np.pi*0.3).move_to([-a,-a,0])).move_to([0,0.5,0])

        self.play(Transform(ML,ML2))

        ##########
        self.next_slide()

        rmv_all(self,[texts[0]])
        self.add(texts[1])
        mol10 = VGroup(*[Circle(0.05, fill_opacity=1).move_to([0.3*np.cos(2*np.pi*i/6),0.3*np.sin(2*np.pi*i/6),0]) for i in range(6)],\
                      *[Line([0.3*np.cos(2*np.pi*i/6),0.3*np.sin(2*np.pi*i/6),0],\
                        [0.3*np.cos(2*np.pi*(i+1)/6),0.3*np.sin(2*np.pi*(i+1)/6),0],color=RED) for i in range(6)],\
                        *[Circle(0.05, fill_opacity=1).move_to([0.6*np.cos(2*np.pi*i/6),0.6*np.sin(2*np.pi*i/6),0]) for i in range(6)],\
                        *[Line([0.3*np.cos(2*np.pi*i/6),0.3*np.sin(2*np.pi*i/6),0],[0.6*np.cos(2*np.pi*i/6),0.6*np.sin(2*np.pi*i/6),0],color=RED) for i in range(6)])

        mol = MLpoint(mol10, "?").move_to([-4,0.5,0])
        self.add(mol)
        self.wait(0.25)
        self.play(FadeOut(mol, target_position=[0,0.5,0]))
        
        mol_ = MLpoint(mol10.move_to([0,0,0]), "2.8").move_to([4,0.5,0])
        self.play(FadeIn(mol_, target_position=[0,0.5,0]))
        self.wait(0.5)





# class scene(ThreeDScene):
#     def construct(self):
#         t1 = Bullet_add(self,"hello",[-4,0,0])
#         self.add_fixed_in_frame_mobjects(Text("Hellooooo").move_to([-2,0,0]))
#         self.begin_ambient_camera_rotation(0.65,"phi")
#         # self.begin_3dillusion_camera_rotation(0,65)
#         A = VGroup(*[Sphere(0.2, resolution=(4,4)).move_to([i,j,k]) for i in [0,1] for j in [0,1] for k in [0,1]]).move_to([2,0,0])
#         self.play(FadeIn(A))
#         # self.play(AnimationGroup(Rotate(A,PI/2, axis=UP), run_time=1))
#         self.wait(1)
#         self.stop_ambient_camera_rotation("phi")
#         # self.stop_3dillusion_camera_rotation()
        
#         self.wait(1)

class Step1(ThreeDScene):
    def construct(self):
        config.disable_caching = True

        self.camera.background_color = BLACK

        # self.camera.move_to([-3,0,0])

        Title = Text("Step 1 : Mapping", font_size=font_title).move_to([0,3.5,0])
        self.add_fixed_in_frame_mobjects(Title)
        # sn = slide_number(self,8)
        sn = Text("8/13", font_size=16).move_to([5.75, -3.5, 0])
        self.add_fixed_in_frame_mobjects(sn)
        t1 = Text("Current constraints to be applicable on neutral atoms device", font_size=24)
        t2 = Text("Unit disk graph", font_size=24)
        t3 = Text("2D graph", font_size=24  )
        # im = ImageMobject("CodeProj.JPG").move_to([-3,0,0])
        # self.add_fixed_in_frame_mobjects(im)
       
        self.add_fixed_in_frame_mobjects(t1.move_to(-t1.get_left()-t1.get_top()+t1.get_center()+[-6,3,0]))
        self.add_fixed_in_frame_mobjects(t2.move_to(-t2.get_left()-t2.get_top()+t2.get_center()+[-5,2.5,0]))
        self.add_fixed_in_frame_mobjects(t3.move_to(-t3.get_left()-t3.get_top()+t3.get_center()+[-5,2,0]))
        self.add_fixed_in_frame_mobjects(Circle(0.05, fill_opacity=1).set_color(BLUE).move_to([-5.2,2.35,0]))
        self.add_fixed_in_frame_mobjects(Circle(0.05, fill_opacity=1).set_color(BLUE).move_to([-5.2,1.85,0]))

        code_font = 18
        code_font_latex = 26
        dict_color = {'for' :GREEN,  '=':PURPLE, '-':PURPLE, '+':PURPLE, '(':BLUE, ')':BLUE, '[':BLUE, ']':BLUE, 'def':GREEN, 'return':GREEN}
        code = [Text("def  V(X):", font_size=code_font, t2c=dict_color),\
                Tex("V", "  = ", "$\\sum_{(i,j)}\\frac{C}{|x_i-x_j|^2}$",font_size=code_font_latex),\
                Tex("V", " += ", "$\\frac{1}{2}K\\sum_{\\langle i,j\\rangle}(|x_i-x_j|-d_{i,j})^2$", font_size=code_font_latex),\
                Tex("V", " += ", "$\\frac{1}{2}H(\\mathbf{n}\\cdot\\mathbf{x})^2$", font_size=code_font_latex),\
                Text("return  V", font_size=code_font, t2c=dict_color),\
                Text(" ", font_size=code_font, t2c=dict_color),\
                Text("def  F(X):", font_size=code_font, t2c=dict_color),\
                Tex("$\cdots$", font_size=code_font_latex),\
                Text("return  F", font_size=code_font, t2c=dict_color),\
                Text(" ", font_size=code_font, t2c=dict_color),\
                Text("coords  =  minimize(V,  grad=-F,  x0=X)", font_size=code_font, t2c=dict_color)]
        alinea = [0,1,1,1,1,0,0,1,1,0,0]
        interligne = [1,0.55,0.1,-0.35,-0.8,-1.15,-1.5,-1.85,-2.2,-2.55,-2.55-0.35]
        code[1][1].set_color(PURPLE)
        code[2][1].set_color(PURPLE)
        code[3][1].set_color(PURPLE)
        self.add_fixed_in_frame_mobjects(*[code[i].move_to(code[i].get_center()-code[i].get_left()+[-6,interligne[i],0]+[0.45*alinea[i],0,0]) for i in range(len(code))])

        # self.add_fixed_in_frame_mobjects(t4.move_to(-t4.get_left()-t4.get_top()+t4.get_center()+[-5,1.5,0]))

        POS = [0,3,0]

        coords = np.array([-0.8275,1.9119,1.7466,-1.0893,-1.6463,-0.6386,-0.7406,-0.1054,0.9215,-1.9138,2.3427,-0.0629,-3.6372,2.6469,-1.4029,0.0916,1.194,3.5778,1.1316,2.1799,0.8475,-1.4887,-0.7217,0.1313,-2.963,-0.4816,0.1188,-3.605,0.6444,-0.1928,-2.9812,1.9585,-0.561,-3.5373,-1.2541,0.3703,-4.6089,0.6003,-0.1747,0.2475,1.6943,4.2199,-0.7254,0.587,4.0592,1.1547,2.7349,0.0559,1.9952,1.4408,0.531,-1.1622,4.0236,2.0904,-3.3025,4.7586,-1.7466,0.8275,-1.9119,-1.7466]).reshape(-1,3)
        coords_ = np.array([0.06985073608313107,0.6362093769414349,0.19521839654512646,-0.5830111410666922,-0.7289925675704391,-0.6151133017428477,-0.19166287035498714,0.1690841732487019,-0.11172026562763296,-0.40686206363229427,0.8617319749833968,-0.12583818956711143,-1.1009912292032182,1.6427997876438771,-0.49309313259798426,0.3849727249752732,0.12236691860591695,0.3266864724329003,0.5259298995406739,0.7863084564063232,0.583381492883584,-0.5641422055815086,-0.143128761596893,-0.4707167534567345,-1.0244171806931848,0.10296953879464536,-0.7744254870637236,-1.181192769470426,0.6859018648312409,-0.7673683532956102,-0.8722970697900717,1.0868387951268357,-0.4382101953136264,-1.4060395155186467,-0.19212644452222724,-1.1367475074877307,-1.6579093148244368,0.8367816412096649,-1.104953985022397,0.8606061066418931,-0.039655572817813164,0.6609622674529562,0.44050867668441224,-0.47199619545531574,0.23831153771394298,0.655285917191794,1.3325416090270739,0.8049869423665147,1.006404247660305,0.6992099414913796,0.9380128559190493,0.03655053453827522,1.2423536603007779,0.30350597991602263,-1.341331693477645,2.192165477674977,-0.5584996550565545,-0.6170000778273629,-1.3108855233552756,-0.7703973973432577]).reshape(-1,3)
        bond = np.array([0,2,1,7,2,7,3,0,4,10,5,0,6,0,7,8,8,9,9,10,10,3,11,8,12,9,13,5,14,5,15,6,16,6,17,0,18,4,19,1]).reshape(-1,2)

        # lines = [Line(coords[bond[j][0],:], coords[bond[j][1],:], color=BLUE,stroke_width=10) for j in range(len(bond))]
        lines = [Cylinder(radius=0.1, height=np.linalg.norm(coords[bond[j][0],:]-coords[bond[j][1],:]), resolution=(8, 4),\
                direction=(coords[bond[j][0],:]-coords[bond[j][1],:])/np.linalg.norm(coords[bond[j][0],:]-coords[bond[j][1],:]))\
                .move_to((coords[bond[j][0],:]+coords[bond[j][1],:])/2)      for j in range(len(bond))]
        spheres = [Sphere(1, fill_opacity=1, resolution=(8,8)).move_to([coords[i,:]]).set_color(RED).scale(0.4) for i in range(len(coords))]
        mol = VGroup(*lines,\
                     *spheres).move_to(POS).scale(0.5)
        
        lines2 = [Cylinder(radius=0.06, height=np.linalg.norm(coords_[bond[j][0],:]-coords_[bond[j][1],:]), resolution=(8, 4),\
                direction=(coords_[bond[j][0],:]-coords_[bond[j][1],:])/np.linalg.norm(coords_[bond[j][0],:]-coords_[bond[j][1],:]))\
                .move_to((coords_[bond[j][0],:]+coords_[bond[j][1],:])/2)      for j in range(len(bond))]
        spheres2 = [Sphere(1, fill_opacity=1, resolution=(8,8)).move_to([coords_[i,:]]).set_color(RED).scale(0.2) for i in range(len(coords))]
        mol_ = VGroup(*lines2,\
                      *spheres2).move_to(POS).scale(0.9)

        self.set_camera_orientation(theta=0, phi=np.pi/2-2*0.65)

        self.add(*lines)
        self.add(*spheres)
        self.wait(0.5)

        a = np.array([-0.27364073,  0.96183198,  0.        ])
        b = np.array([-0.74773274, -0.2127296 , -0.62900069])
        p1 = -2*a+2*b
        p2 = -2*a-2*b
        p3 = 2.3*a-2*b
        p4 = p1+p3-p2


        
        self.begin_ambient_camera_rotation(0.65,"phi")

        self.wait(3)
        self.play(FadeIn(Polygon(p1,p2,p3,p4)\
                 .set_opacity(0.4).set_color(BLUE).move_to(POS)))
        
        self.wait(1)

        self.play(Transform(mol, mol_), run_time=1.5)
        self.wait(1.75)
        self.stop_ambient_camera_rotation("phi")
        self.wait(1)
        
        


class Homology(Scene):
    def construct(self):
        sn = slide_number(self,5)

        coords = np.array([[0,0,0],[0,1,0],[1,0.35,0],[0.5,2,0],[1.5,2.5,0],[3.3,2,0],[2.2,1.1,0]])
        coords = coords-np.mean(coords, axis=0)+np.array([0,1,0])
        Gram = np.zeros((7,7))
        for i in range(7):
             for j in range(i+1,7):
                  Gram[i,j] = np.linalg.norm(coords[i,:]-coords[j,:])/2
        I = np.argsort(Gram.reshape(-1))
        pairs = np.zeros((7*3,2), dtype=int)
        dist = np.zeros((7*4))
        for i in range(7*4,7*7):
             dist[i-7*4] = Gram[I[i]//7,I[i]%7]
             pairs[i-7*4,:] = np.array([I[i]//7,I[i]%7],dtype=int)


        points = VGroup(*[Circle(0.1, fill_opacity=1, color=GREEN).move_to(coords[i,:]) for i in range(len(coords))])
        circles = VGroup(*[Circle(0.1, fill_opacity=1, color=GREEN).move_to(coords[i,:]).set_opacity(0.2) for i in range(len(coords))])

        self.add(points, circles)
        self.wait(1)

        cycle1 = Polygon(*[coords[i,:] for i in [1,3,4,6,2]], color=RED, stroke_width=5)
        cycle2 = Polygon(*[coords[i,:] for i in [3,4,6,2]], color=RED, stroke_width=5)

        texts = [Text("Here is our data points cloud", font_size=24),\
                 Text("The sphere of influence of each points will continuously grow", font_size=24),\
                 Text("Connections and surfaces appear", font_size=24),\
                 Text("Cycles emerge", font_size=24),\
                 Text("This information of creation and destruction of connections and cycles\n        build the persistent diagram, and can be used as feature", font_size=24)]

        def show(texts, arr, wait_time, pos):
             for i in range(len(arr)):
                self.play(FadeIn(texts[arr[i]].move_to(pos[i]), run_time=0.25))
                self.wait(wait_time[i])
                self.play(FadeOut(texts[arr[i]], run_time=0.25))

        for j in range(11):
            # Texts
            if j==0:
                show(texts,[0,1],[2,2],[[0,-2.75,0],[0,-2.75,0]])
                self.wait(2)
            if j==1:
                show(texts,[2],[1.5],[[0,-2.75,0]])
            # if j==5:
            #     show(texts,[3],[1.5],[[0,-2.75,0]])
            if j==8:
                show(texts,[3],[2],[[0,-2.75,0]])
                


            if j==0:
                self.play(Transform(circles, VGroup(*[Circle(dist[j], fill_opacity=1, color=GREEN).move_to(coords[i,:]).set_opacity(0.2) for i in range(len(coords))]))\
                        , rate_func=linear, run_time=4*(dist[j]-0.1))
            else:
                self.play(Transform(circles, VGroup(*[Circle(dist[j], fill_opacity=1, color=GREEN).move_to(coords[i,:]).set_opacity(0.2) for i in range(len(coords))]))\
                        , rate_func=linear, run_time=4*(dist[j]-dist[j-1]))
            self.add(Line(coords[pairs[j,0],:],coords[pairs[j,1],:], color=GREEN,stroke_width=5))

            if j==4:
                 self.add(Polygon(coords[0,:],coords[1,:],coords[2,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
            if j==7:
                 self.add(cycle1)
            if j==8:
                 self.remove(cycle1)
                 self.add(cycle2)
                 self.add(Polygon(coords[3,:],coords[1,:],coords[2,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
            if j==9:
                 self.add(Polygon(coords[5,:],coords[6,:],coords[4,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
            if j==10:
                 self.remove(cycle2)
                 self.add(Polygon(coords[3,:],coords[6,:],coords[4,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
                 self.add(Polygon(coords[3,:],coords[6,:],coords[2,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))

            if j in [0,4,7,10]:#[0,1,4,6,7,8,9]:
                 self.wait(1)


        show(texts,[4],[4],[[0,-2.75,0]])

        self.wait(1)


class MLtext(Scene):
    def construct(self):
        Title = Text("Prediction Model", font_size=font_title)
        self.add(Title.move_to([0,3.5,0]))
        sn = slide_number(self,4)

        self.wait(1)
        t1 = Bullet_add(self,"With machine learning techniques, new molecules can be efficiently screened \nas potential efficient carbon sequestration materials",[-6,2,0])
        t2 = Bullet_add(self,"This allows to test a large number of theoretical molecules,\nthat can be latter tested experimentally",[-6,1,0])
        t3 = Bullet_add(self,"The usefulness of the model relies on its accuracy",[-6,0,0])
        t4 = Bullet_add(self,"But the latter strongly depends on the input features",[-6,-1,0])
        txt = "Persistent homology features gets more and more interest for graph related \napplications (notable molecular problems)"
        text = Text(txt, font_size=24, t2w={'Persistent homology':BOLD})
        circle = Circle(0.04, fill_opacity=1, color=BLUE).move_to([-6,-2,0])
        self.add(circle)
        self.add(text.move_to(text.get_center()-text.get_top()-text.get_left()+[-6,-2,0]+[0.2,0.15,0]))
        self.wait(1)


class Quantum(Scene):
    def construct(self):
 
        # self.add(sommaire_sketch)
        # self.add(sommaire_text)
        # self.wait(1)
        # RR2 = Rectangle(height=4,width=6,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([-3,0,0])
        # RR1 = Rectangle(height=4,width=4,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([5,0,0])
        # self.play(AnimationGroup(FadeIn(RR1),\
        #                          FadeIn(RR2)))
        # self.wait(1)
        # self.play(FadeOut(sommaire_sketch, run_time=0))
        # self.play(FadeOut(sommaire_text, run_time=0))
        # self.wait(0.5)
        Title = Text("Quantum Approach", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        sn = slide_number(self,6)
        self.wait(0.1)
        
        t1 = Bullet_add(self,"Strong similiarities between the persistent homology and the Rydberg blockade",[-6,2,0])
        t2 = Bullet_add(self,"This inspired us to use neutral atoms quantum computer",[-6,1,0])
        t3 = Bullet_add(self,"Extract topological features from the dynamics at different Rydberg radii",[-6,0,0])
        t4 = Bullet_add(self,"This topological features has for objective to enrich the predictive model",[-6,-1,0])
        self.wait(1)


class Outlook(Scene):
    def construct(self):

        Title = Text("Project outlook", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        self.wait(1)

        # t1 = Bullet(self,"This method has the advantage that computing the dynamic of a \
        #             \nquantum many-body is extremely difficult on a classical computer",[-6,2.5,0])
        # t2 = Bullet(self,"complexity ?", [-6,1.75,0])
        # t3 = Bullet(self,"With more qubits, one could use this persistent homology feature\
        #             \nfor different appplications, with larger molecule such as proteins", [-6,1,0])

        def boxtext(title, texts, pos):
            title_rect = Text(title, font_size=24, weight=BOLD).move_to(pos)
            rect = RoundedRectangle(corner_radius=0.5, height=4.5, width=4.0, fill_opacity=0.3, fill_color=GREEN).move_to([pos[0],0.25,0])
            return VGroup(rect,title_rect\
            ,*[Text(texts[i], font_size=18).move_to(title_rect.get_center()-Text(texts[i], font_size=18).get_left()-Text(texts[i], font_size=18).get_top()+[-1.75,-0.5-1.75*i,0]) for i in range(len(texts))])

        t1 = boxtext("Benefits", ["Computing the dynamic of a \nquantum many-body is \nextremely difficult on a \nclassical computer","Complexity advantage"],\
                    [-4.5,2,0])
    
        t2 = boxtext("Scalibility", ["With more qubits, one could \nuse this persistent homology \nfeature for different \nappplications, with lager \nmolecules such as proteins",\
                                    "Having a neutral atoms device \nallowing to set up a 3D array \nwould simplify the \nmodelisation"],\
                     [0,2,0])
        t3 = boxtext("Today's maturity",["Most of the MOFs have less \nthan 140 atoms, and therefore \nare simulable on Pasqal's \ncurrent device"],\
                     [4.5,2,0])
        
        
        self.play(AnimationGroup(FadeIn(t1),FadeIn(t2), FadeIn(t3), lag_ratio=0.5))
        self.wait(7)


class Roadmap(Scene):
    def construct(self):

        Title = Text("Roadmap", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        sn = slide_number(self,11)
        self.wait(1)

        t = Text("MVP : Improve the accuracy of the ML workflow with small molecules", font_size = 18).move_to([-2.75,2.75,0])
        self.add(t)
        t1 = Text("63% of dataset are less than 140 atoms, algorithm currently implementable", font_size = 18, t2w={'currently':BOLD}).move_to([-2.25,2.25,0])
        self.add(t1)
        

        nx = 5
        ny = 5
        lx = 8
        ly = 4
        axes = Axes(
            x_range=[0, 1, 1/nx],
            y_range=[0, 1, 1/(ny+1)],
            x_length=lx,
            y_length=ly,
            axis_config={"color": BLUE},
            x_axis_config={
                # "numbers_to_include": np.arange(1900, 2022, 1/nx),
                # "numbers_with_elongated_ticks": np.arange(-10, 10.01, 2),
            },
            tips=False,
        )


        self.play(Create(axes))

        textsy = ["Projection", "Simulation", "Features from\n       dynamic", "Energy balance", "Machine learning"]
        labelsy = VGroup(*[Text(textsy[i], font_size=16).move_to(\
            Text(textsy[i], font_size=16).get_center()-Text(textsy[i], font_size=16).get_right()+[-lx/2*1.05, (ny-i)/(ny+1)*ly-ly/2,0]) for i in range(ny)])

        textsx = ["Phase 1", "Phase 2", "Phase 3", "Final", "MVP"]
        labelsx = VGroup(*[Text(textsx[i], font_size=16).move_to([-lx/2+lx*i/nx+lx/nx/2, -ly/2*1.1,0]) for i in range(nx)])

        self.play(AnimationGroup(Write(labelsy),Write(labelsx)))

        arr = [[0.2,3],[0.2,4],[1,7.5],[4,6.25],[5,8]]
        rectangles = VGroup(*[Rectangle(height=ly/(ny+1)*0.8, width=0).move_to([(arr[i][1]+arr[i][0])/2-lx/2,(ny-i)/(ny+1)*ly-ly/2,0]) for i in range(ny)])
        rectangles2 = VGroup(*[Rectangle(height=ly/(ny+1)*0.8, width=arr[i][1]-arr[i][0], fill_opacity=0.5).move_to([(arr[i][1]+arr[i][0])/2-lx/2,(ny-i)/(ny+1)*ly-ly/2,0]) for i in range(ny)])
        rectangles.set_color_by_gradient(BLUE, GREEN, YELLOW)
        rectangles2.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Transform(rectangles,rectangles2))
        self.wait(1)
        line1 = Line([4*lx/nx-lx/2,-ly/2,0],[4*lx/nx-lx/2,-ly/2,0], color=RED)
        line2 = Line([4*lx/nx-lx/2,-ly/2,0],[4*lx/nx-lx/2,ly/2,0], color=RED)
        self.play(Transform(line1,line2))
        self.wait(1)

        b = Brace(Line([-lx/2,-ly/2*1.2,0],[-lx/2+4*lx/nx,-ly/2*1.2,0]),sharpness=1)
        text_acc = Text("Hackathon ~ 4 weeks",font_size=18).move_to([-lx/2+2*lx/nx,-ly/2*1.5,0])
        text_end = Text("End ~ 6 weeks",font_size=18).move_to([-lx/2+5*lx/nx,-ly/2*1.5,0])
        self.play(FadeIn(b))
        self.play(Write(text_acc))
        self.play(Write(text_end))
        self.wait(1)




class Step2(Scene):
    def construct(self):
        config.disable_caching = True

        Title = Text("Step 2 : Dynamics", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        t1 = Text("Detect changes in the time evolution", font_size=24)
        self.add(t1.move_to(t1.get_center()-t1.get_left()+[-2,3,0]))
        sn = slide_number(self,9)

        code_font = 18
        dict_color = {'for' :GREEN, 'in':PURPLE, '=':PURPLE, '(':BLUE, ')':BLUE, '[':BLUE, ']':BLUE}
        code = [Text("for  R_b  in  R_bvals:", font_size=code_font, t2c=dict_color),\
                Text("   Graph = G(R_b)", font_size=code_font, t2c=dict_color),\
                Text("  for  t  in  t_vals:", font_size=code_font, t2c=dict_color),\
                Text("      Evolve(Graph,t)", font_size=code_font, t2c=dict_color),\
                Text("      Obs[t]  =  Measure(Graph)", font_size=code_font, t2c=dict_color),\
                Text("  Spectrum[Rb]  =  FFT(Obs)", font_size=code_font, t2c=dict_color)]
        alinea = [0,1,1,2,2,1]

        self.add(*[code[i].move_to(code[i].get_center()-code[i].get_left()+[-6.5,1-0.35*i,0]+[0.45*alinea[i],0,0]) for i in range(len(code))])

        r = 0.1
        hexa = VGroup(*[Circle(r, fill_opacity=1,color=GREEN).move_to([np.cos(2*PI/6*i),np.sin(2*PI/6*i),0]) for i in range(6)]).move_to([0,0,0])
        circles = VGroup(*[Circle(r, fill_opacity=1,color=GREEN).set_opacity(0.2).move_to([np.cos(2*PI/6*i),np.sin(2*PI/6*i),0]) for i in range(6)]).move_to([0,0,0])
        im = ImageMobject("C6__.png").move_to([5,0,0])

        line_left = -1.7
        line_right = 2
        line = Line([line_left,0,0],[line_right,0,0]).move_to([5,-1.7,0])
        lines = VGroup(*[Line([np.cos(2*PI/6*i),np.sin(2*PI/6*i),0],[np.cos(2*PI/6*(i+1)),np.sin(2*PI/6*(i+1)),0], color=GREEN) for i in range(6)]).move_to([0,0,0])
        lines2 = VGroup(*[Line([np.cos(2*PI/6*i),np.sin(2*PI/6*i),0],[np.cos(2*PI/6*(i+j)),np.sin(2*PI/6*(i+j)),0], color=GREEN)\
                         for j in range(2,5) for i in range(6)]).move_to([0,0,0])

        self.add(im)
        self.add(hexa)
        self.add(circles)
        self.add(line)
        self.wait(1)

        ##########
        self.next_slide()
        
        t=ValueTracker(17)
        code[1].add_updater(lambda z: z.become(Text("Graph = G("+str(np.round(10*t.get_value())/10)+")",font_size=code_font, t2c=dict_color)\
                                               .move_to(code[1].get_center()-code[1].get_left()+[-6.5,1-0.35*1,0]+[0.45*alinea[1],0,0])))

        # self.play(t.animate.set_value(8.1))

        self.play(AnimationGroup(t.animate.set_value(7.9), Transform(circles, VGroup(*[Circle(1/2, fill_opacity=1, color=GREEN).move_to([np.cos(2*PI/6*i),np.sin(2*PI/6*i),0]).set_opacity(0.2) for i in range(6)]).move_to([0,0,0]), rate_func=linear)\
                ,Transform(line,Line([line_left,0,0],[line_right,0,0]).move_to([5,0.35,0]) ,rate_func=linear), run_time=4*(1/2-0.1)))
        self.add(lines)
        self.play(Circumscribe(line))
        
        self.wait(1)

        self.play(AnimationGroup(t.animate.set_value(3.8),Transform(circles, VGroup(*[Circle(1, fill_opacity=1, color=GREEN).move_to([np.cos(2*PI/6*i),np.sin(2*PI/6*i),0]).set_opacity(0.2) for i in range(6)]).move_to([0,0,0]), rate_func=linear)\
                ,Transform(line,Line([line_left,0,0],[line_right,0,0]).move_to([5,1.3,0]) ,rate_func=linear), rate_func=linear, run_time=4*(1-1/2)))
        self.add(lines2)

        self.wait(1)


class Steps(Scene):
    def construct(self):
        config.disable_caching = True
        Title = Text("Quantum Solution", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        sn = slide_number(self,7)
        self.wait(0.1)
        t4 = Text("Leverage neutral atoms interactions and dynamics to provide \n               structural information from a molecule​", font_size=24)
        self.add(t4.move_to(t4.get_center()-t4.get_left()+[-4.75,2.5,0]))
        t1 = Text("Step 1 : Mapping", font_size=24)
        self.add(t1.move_to(t1.get_center()-t1.get_left()+[-5,1,0]))
        t2 = Text("Step 2 : Dynamics", font_size=24)
        self.add(t2.move_to(t2.get_center()-t2.get_left()+[-5,-0.25,0]))
        t3 = Text("Step 3 : Classical Regression", font_size=24)
        self.add(t3.move_to(t3.get_center()-t3.get_left()+[-5,-1.5,0]))
        self.wait(0.5)



class Step3(Scene):
    def construct(self):
        Title = Text("Step 3 : Classical Regression", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        sn = slide_number(self,10)
        self.wait(0.5)

        t3 = Text("Quantum features are added to the model to infer carbon affinity", font_size=24)
        self.add(t3.move_to(t3.get_center()-t3.get_left()+[-5.5,2.5,0]))

        im = ImageMobject("MLPitchFig.png").scale(0.2).move_to([-3,0,0])
        self.add(im)
        ref = Text("[1] Ibrahim B. Orhan and al. Accelerating the prediction of CO2 capture at low \npartial pressures in metal-organic frameworks using \nnew machine learning descriptors.", font_size=16)
        self.add(ref.move_to(ref.get_center()-ref.get_left()+[-6,-3,0]))
        footnote = Text("From [1], without including the quantum features", font_size=18)
        self.add(footnote.move_to(footnote.get_center()-footnote.get_left()+[-0.5,0,0]))
        self.wait(0.5)

class Conclusion(Scene):
    def construct(self):
        Title = Text("Conclusion", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        sn = slide_number(self,13)
        self.wait(0.5)

        t1 = Text("Key points :", font_size=24)
        self.add(t1.move_to(t1.get_center()-t1.get_left()+[-5.5,2,0]))
        t2 = Bullet_add(self,"Leverage neutral atoms interactions and dynamics to provide \nstructural information from a molecule",[-5.5,1.5,0])
        t3 = Bullet_add(self,"Inspired from state-of-art MOF analysis",[-5.5,0.75,0])
        t7 = Bullet_add(self,"Hybrid workflow",[-5.5,0,0])

        t4 = Text("Next steps :", font_size=24)
        self.add(t4.move_to(t4.get_center()-t4.get_left()+[-5.5,-1,0]))
        t5 = Bullet_add(self,"Study new observables",[-5.5,-1.75,0])
        t6 = Bullet_add(self,"Try other projections with differents conservation properties",[-5.5,-2.5,0])
        t5 = Bullet_add(self,"Extend the algorithm on larger molecules, such as proteins",[-5.5,-3.25,0])
        

        self.wait(1)


class Energy(Scene):
    def construct(self):
        config.disable_caching = True
        Title = Text("Energy", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        sn = slide_number(self,12)
        im = ImageMobject("ComplexityFig2.png").scale(0.2).move_to([-3,0,0])  
        self.add(im)

        t1 = Text("Joliot Curie 7Pflops", font_size=18)
        self.add(t1.move_to(t1.get_center()-t1.get_left()+[0,1,0]))
        t2 = Text("Fresnel 140 qubits", font_size=18)
        self.add(t2.move_to(t2.get_center()-t2.get_left()+[3,1,0]))
        t3 = Text("~10 times faster", font_size=18)
        self.add(t3.move_to(t3.get_center()-t3.get_left()+[0,0,0]))
        t4 = Text("~5 times less C02", font_size=18)
        self.add(t4.move_to(t4.get_center()-t4.get_left()+[3,0,0]))
        self.wait(1)

class TY(Scene):
    def construct(self):
        self.play(Write(Text("Thank you")))
        self.wait(1)