from manim import *
import numpy as np

def Bullet(self, txt, pos, e=0.2, r=0.04, font=24):
    text = Text(txt, font_size=font)
    circle = Circle(r, fill_opacity=1, color=BLUE).move_to(pos)
    self.play(Create(circle), run_time = 0.4)
    self.play(Write(text.move_to(text.get_center()-text.get_left()-text.get_top()+pos+[e,0.15,0])), run_time=1)
    return VGroup(text, circle)

def Bullet2(self, txt, pos, e=0.2, r=0.04, font=24):
    pos[0] += 0.4
    text = Text(txt, font_size=font)
    circle = Circle(r*0.6, fill_opacity=0, color=BLUE).move_to(pos)
    self.play(Create(circle), run_time = 0.4)
    self.play(Write(text.move_to(text.get_center()-text.get_left()-text.get_top()+pos+[e,0.15,0])), run_time=1)
    return VGroup(text, circle)

def rmv(self,obj):
    self.play(FadeOut(obj, run_time=0))

def rmv_all(self,obj):
    self.play(AnimationGroup(*[FadeOut(obj[i], run_time=0.25) for i in range(len(obj))]))

class Video(ThreeDScene):
    def construct(self):
        self.camera.background_color = BLACK
        font_title = 36
        fill_opacity_black_rectangle = 0.75

        Title1 = Text("MATERIAL CHARACTERISATION", font_size=40,weight=BOLD).move_to([0,1,0])
        Title2 = Text("FOR CO2 CAPTURE", font_size=40,weight=BOLD).move_to([0,0.5,0])
        Subtitle = Text("Presentation video", font_size=24).move_to([0,-0.5,0])
        Title = VGroup(Title1,Title2,Subtitle)
        name = Text("CuriousTurtles",color=BLUE, font_size=24).move_to([0,-1,0])
        self.add(Title)
        self.wait(1)
        self.play(Write(name))
        self.wait(1)

        self.play(FadeOut(Title),run_time=0.5 )
        self.play(FadeOut(name),run_time=0.5 )
        self.wait(0.5)

        Title = Text("Summary", font_size=font_title)
        self.add(Title.move_to([0,3.5,0]))
        sommaire_sketch = VGroup(*[Line([-4.5*(1-i/3)+4.5*i/3+0.2,0,0],[-4.5*(1-(i+1)/3)+4.5*(i+1)/3-0.2,0,0], stroke_width=5) for i in range(3)],\
                                 *[Circle(0.2, fill_opacity=0.5).move_to([-4.5*(1-i/3)+4.5*i/3,0,0]) for i in range(4)])
        sommaire_text = VGroup(Text("Problem statement", font_size=18).move_to([-4.5,-0.5,0]),\
                               Text("Temporary solution", font_size=18).move_to([-1.5,-0.5,0]),\
                               Text("Quantum approach", font_size=18).move_to([1.5,-0.5,0]),\
                               Text("Project outlook", font_size=18).move_to([4.5,-0.5,0]))
        self.play(AnimationGroup(*[Create(sommaire_sketch[i]) for i in [3,0,4,1,5,2,6]], lag_ratio=0.5, run_time=2))
        self.play(AnimationGroup(*[Write(sommaire_text[i]) for i in range(4)], lag_ratio=0.5))      
        self.wait(1)
        RR = Rectangle(height=4,width=10,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([2,0,0])
        self.play(FadeIn(RR))
        self.wait(1)
        rmv_all(self,[sommaire_sketch,sommaire_text,Title,RR])
        self.wait(0.5)

        Title = Text("Problem statement", font_size=font_title)
        self.add(Title.move_to([0,3.5,0]))

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
        rectangles2 = VGroup(*[Rectangle(width=lx/nx, height=h[i]).move_to([i/nx*lx-lx/2+lx/nx/2,-ly/2+h[i]/2,0]) for i in range(nx)])
        # self.add(rectangles)
        self.wait(0.5)
        self.play(Transform(rectangles,rectangles2))
        self.wait(0.5)
        Graph = VGroup(Plot, rectangles)
        
        self.play(Graph.animate.shift([-3,0,0]))

        r = 0.04
        e = 0.2


        t1 = Bullet(self, "Exponential increase of CO2 emission", [0.6,2,0], e, r)
        t2 = Bullet(self, "Too profound changes are needed \nin many hard to abate sectors", [0.6,1,0], e, r)
        t3 = Bullet(self, "Mitigate the effect in the waiting \nof a sustainable solution", [0.6,0,0], e, r)
        self.wait(3)

        # rmv(self,Graph)
        # rmv(self,t1)
        # rmv(self,t2)
        # rmv(self,t3)
        # rmv(self,Title)
        rmv_all(self,[Graph, t1, t2, t3, Title])
        self.wait(2)

        ### Slide text MOF ###

        Title = Text("Summary", font_size=font_title)
        self.add(Title.move_to([0,3.5,0]))
        self.add(sommaire_sketch)
        self.add(sommaire_text)
        self.wait(1)
        RR1 = Rectangle(height=4,width=6,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([3,0,0])
        RR2 = Rectangle(height=4,width=4,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([-5,0,0])
        self.play(AnimationGroup(FadeIn(RR1),\
                                 FadeIn(RR2)))
        self.wait(1)
        rmv_all(self,[sommaire_sketch,sommaire_text,Title,RR1,RR2])
        self.wait(0.5)

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
        RR = Rectangle(width=20, height=10, fill_color=BLACK, stroke_width=0, fill_opacity=0.5)
        self.add(RR)

        Title = Text("Temporary solution", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        t1 = Bullet(self,"One way to slow dow the effect of the climate \nchange is to capture the carbon in the atmosphere", [-6,1.5,0])
        self.wait(2)
        t2 = Bullet(self,"This can be done by nanoporous material such as \nMetallic Organic Framework (MOF)", [-6,0.5,0])
        self.wait(2)
        t5 = Bullet(self,"Such solution would be rather straightfoward to set up", [-6,-0.5,0])
        self.wait(2)
        t3 = Bullet(self,"Experimental tests on molecules can be costly and slow", [-6,-1.5,0])
        self.wait(2)
        t4 = Bullet(self,"To find new good candidates, machine learning techniques have been used", [-6,-2.5,0])
        self.wait(2)

        # rmv(self,t1)
        # rmv(self,t2)
        # rmv(self,t3)
        # rmv(self,t4)
        # rmv(self,t5)
        # rmv(self,crystal)
        # rmv(self,Title)
        rmv_all(self,[t1,t2,t3,t4,t5,crystal,Title,RR])
        self.wait(3)

        ### Slide ML ###
        Title = Text("Prediction model", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)

        def MLpoint(mol, val, L=1.5):
             return VGroup(mol,RoundedRectangle(corner_radius=0.25, height=L, width=L, color=RED),\
            RoundedRectangle(corner_radius=0.25, height=L, width=L, color=RED).set_opacity(0.25),\
            Text(val, font_size=16).move_to([-L*0.7/2,L*0.7/2,0]))

        def Gauge(theta=np.pi*0.9):
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
                      Line([-0.3,0,0],[0,0,0],color=RED),Line([0.3,0,0],[0,0,0],color=RED))
        
        mol9 = VGroup(*[Circle(0.05, fill_opacity=1).move_to([0.3*np.cos(2*np.pi*i/4),0.3*np.sin(2*np.pi*i/4),0]) for i in range(4)],\
                      *[Line([0.3*np.cos(2*np.pi*i/4),0.3*np.sin(2*np.pi*i/4),0],\
                        [0.3*np.cos(2*np.pi*(i+1)/4),0.3*np.sin(2*np.pi*(i+1)/4),0],color=RED) for i in range(4)],\
                        Circle(0.05, fill_opacity=1).move_to([0.6*np.cos(2*np.pi*2/4),0.6*np.sin(2*np.pi*2/4),0]),\
                        Line([0.3*np.cos(2*np.pi*2/4),0.3*np.sin(2*np.pi*2/4),0],[0.6*np.cos(2*np.pi*2/4),0.6*np.sin(2*np.pi*2/4),0],color=RED))

        mol_arr = [mol1,mol3,mol2,mol9]
        val_arr = ["2.4","1.1","3.0","0.2"]
        mols = VGroup(*[MLpoint(mol_arr[i], val_arr[i]).move_to([-4,3*(1-i/(len(val_arr)-1))-2*i/(len(val_arr)-1),0])\
                         for i in range(len(val_arr))])

        texts = [Text("Experimental data are used to train the model", font_size=24).move_to([0,-3,0]),\
                 Text("Carbon affinity of new molecules can be inferred", font_size=24).move_to([0,-3,0])]

        self.add(mols)
        self.add(ML)
        self.play(FadeIn(texts[0], run_time=0.5))
        self.wait(0.5)
        self.play(AnimationGroup(*[FadeOut(mols[i],target_position=[0,0.5,0]) for i in range(len(mols))], lag_ratio = 0.1))
        self.wait(0.25)
        self.play(FadeOut(texts[0], run_time=0.5))

        ML2 = VGroup(Rectangle(height=3, width=3),\
        Gauge(np.pi*0.1).move_to([a,a,0]),Gauge(np.pi*0.5).move_to([-a,a,0])\
        ,Gauge(np.pi*0.3).move_to([a,-a,0]),Gauge(np.pi*0.9).move_to([-a,-a,0])).move_to([0,0.5,0])

        self.play(Transform(ML,ML2))
        self.wait(1)
        
        mol = MLpoint(Circle(0.05, fill_opacity=1), "?").move_to([-4,0.5,0])
        self.add(mol)
        self.wait(0.25)
        self.play(FadeIn(texts[1], run_time=0.5))
        self.wait(0.25)
        self.play(FadeOut(mol, target_position=[0,0.5,0]))
        
        mol_ = MLpoint(Circle(0.05, fill_opacity=1), "2.8").move_to([4,0.5,0])
        self.play(FadeIn(mol_, target_position=[0,0.5,0]))
        self.wait(0.25)
        self.play(FadeOut(texts[1],run_time=0.5))
        self.wait(0.5)

        # rmv(self,mol_)
        # rmv(self,ML)
        rmv_all(self,[mol_,ML])

        ### Slide text ML ###

        
        self.wait(1)
        t1 = Bullet(self,"With machine learning techniques, new molecules can be efficiently screened \nas potential efficient carbon sequestration materials",[-6,2,0])
        self.wait(1)
        t2 = Bullet(self,"This allow to test a large number of theoretical molecules,\nthat can be latter tested experimentally",[-6,1,0])
        self.wait(1)
        t3 = Bullet(self,"The usefulness of the model relies on its accuracy",[-6,0,0])
        self.wait(1)
        t4 = Bullet(self,"But the latter strongly depends on the input features",[-6,-1,0])
        self.wait(1)
        txt = "Persistent homology features gets more and more interest for graph related \napplications (notable molecular problems)"
        text = Text(txt, font_size=24, t2w={'persistent homology':BOLD})
        circle = Circle(0.04, fill_opacity=1, color=BLUE).move_to([-6,-2,0])
        self.play(Create(circle), run_time = 0.4)
        self.play(Write(text.move_to(text.get_center()-text.get_top()-text.get_left()+[-6,-2,0]+[0.2,0.15,0])), run_time=1)
        self.wait(1)

        # rmv(self, t1)
        # rmv(self, t2)
        # rmv(self, t3)
        # rmv(self, t4)
        # rmv(self,VGroup(text,circle))
        # rmv(self,Title)
        rmv_all(self,[t1,t2,t3,t4,VGroup(text,circle),Title])
        self.wait(3)

        ### Persistent homology ###

        Title = Text("Persistent homology", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)

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

        self.play(FadeIn(points), FadeIn(circles))
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


        polygons = []
        lines = []
        for j in range(11):
            # Texts
            if j==0:
                show(texts,[0,1],[2,2],[[0,-2.75,0],[0,-2.75,0]])
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
            lines.append(Line(coords[pairs[j,0],:],coords[pairs[j,1],:], color=GREEN,stroke_width=5))
            self.add(lines[-1])

            if j==4:
                 polygons.append(Polygon(coords[0,:],coords[1,:],coords[2,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
                 self.add(polygons[-1])
            if j==7:
                 self.add(cycle1)
            if j==8:
                 self.remove(cycle1)
                 self.add(cycle2)
                 polygons.append(Polygon(coords[3,:],coords[1,:],coords[2,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
                 self.add(polygons[-1])
            if j==9:
                 polygons.append(Polygon(coords[5,:],coords[6,:],coords[4,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
                 self.add(polygons[-1])
            if j==10:
                 self.remove(cycle2)
                 polygons.append(Polygon(coords[3,:],coords[6,:],coords[4,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
                 self.add(polygons[-1])
                 polygons.append(Polygon(coords[3,:],coords[6,:],coords[2,:],fill_color = BLUE, fill_opacity=0.5,stroke_width=0))
                 self.add(polygons[-1])

            if j in [0,4,7,10]:#[0,1,4,6,7,8,9]:
                 self.wait(0.75)


        show(texts,[4],[4],[[0,-2.75,0]])

        self.wait(1)
        rmv(self,points)
        rmv(self,circles)
        rmv(self,VGroup(*lines))
        rmv(self,VGroup(*polygons))
        rmv(self,Title)
        
        self.wait(1)


        ### Slide text quantum ###
        
        self.add(sommaire_sketch)
        self.add(sommaire_text)
        self.wait(1)
        RR2 = Rectangle(height=4,width=6,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([-3,0,0])
        RR1 = Rectangle(height=4,width=4,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([5,0,0])
        self.play(AnimationGroup(FadeIn(RR1),\
                                 FadeIn(RR2)))
        self.wait(1)
        self.play(FadeOut(sommaire_sketch, run_time=0))
        self.play(FadeOut(sommaire_text, run_time=0))
        self.wait(0.5)
        Title = Text("Quantum approach", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        self.wait(1)

        t1 = Bullet(self,"Strong similiarities can be seen between the process of growing sphere\
                \nfor the persitent homology, and the quantum effect of the Rydberg blockade",[-6,2,0])
        self.wait(3)
        t2 = Bullet(self,"This resemblance inspired us to use neutral atoms quantum computer\
                \nto extract topological features from the molecule of interest",[-6,1,0])
        self.wait(3)
        t3 = Bullet(self,"From the dynamics of the neutral atoms array at different Rydberg radii,\
                    \none could extract valuable topological features of the molecule",[-6,0,0])
        self.wait(3)
        t4 = Bullet(self,"This topological features has for objective to enrich the predictive model",[-6,-1,0])
        self.wait(4)

        # rmv(self,t1)
        # rmv(self,t2)
        # rmv(self,t3)
        # rmv(self,t4)
        # rmv(self,Title)
        rmv_all(self,[t1,t2,t3,t4,Title,RR1,RR2])
        self.wait(1)

        ### Slide algo ###
        Title = Text("Algorithm", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        self.wait(1)

        t1 = Text("Step 1 : Mapping", font_size=24).move_to([-5,2,0])
        self.add(t1)
        t2 = Bullet(self,"Project the molecule onto a plane without losing the topology",[-6,1.5,0])
        t3 = Bullet(self,"Make sure that the graph created by the molecule is a 'unit disk graph'",[-6,0.95,0])
        self.wait(3)

        rmv_all(self,[t1,t2,t3,Title])
        self.wait(1)

        coords = np.array([-0.8275,1.9119,1.7466,-1.0893,-1.6463,-0.6386,-0.7406,-0.1054,0.9215,-1.9138,2.3427,-0.0629,-3.6372,2.6469,-1.4029,0.0916,1.194,3.5778,1.1316,2.1799,0.8475,-1.4887,-0.7217,0.1313,-2.963,-0.4816,0.1188,-3.605,0.6444,-0.1928,-2.9812,1.9585,-0.561,-3.5373,-1.2541,0.3703,-4.6089,0.6003,-0.1747,0.2475,1.6943,4.2199,-0.7254,0.587,4.0592,1.1547,2.7349,0.0559,1.9952,1.4408,0.531,-1.1622,4.0236,2.0904,-3.3025,4.7586,-1.7466,0.8275,-1.9119,-1.7466]).reshape(-1,3)
        coords_ = np.array([0.06985073608313107,0.6362093769414349,0.19521839654512646,-0.5830111410666922,-0.7289925675704391,-0.6151133017428477,-0.19166287035498714,0.1690841732487019,-0.11172026562763296,-0.40686206363229427,0.8617319749833968,-0.12583818956711143,-1.1009912292032182,1.6427997876438771,-0.49309313259798426,0.3849727249752732,0.12236691860591695,0.3266864724329003,0.5259298995406739,0.7863084564063232,0.583381492883584,-0.5641422055815086,-0.143128761596893,-0.4707167534567345,-1.0244171806931848,0.10296953879464536,-0.7744254870637236,-1.181192769470426,0.6859018648312409,-0.7673683532956102,-0.8722970697900717,1.0868387951268357,-0.4382101953136264,-1.4060395155186467,-0.19212644452222724,-1.1367475074877307,-1.6579093148244368,0.8367816412096649,-1.104953985022397,0.8606061066418931,-0.039655572817813164,0.6609622674529562,0.44050867668441224,-0.47199619545531574,0.23831153771394298,0.655285917191794,1.3325416090270739,0.8049869423665147,1.006404247660305,0.6992099414913796,0.9380128559190493,0.03655053453827522,1.2423536603007779,0.30350597991602263,-1.341331693477645,2.192165477674977,-0.5584996550565545,-0.6170000778273629,-1.3108855233552756,-0.7703973973432577]).reshape(-1,3)
        bond = np.array([0,2,1,7,2,7,3,0,4,10,5,0,6,0,7,8,8,9,9,10,10,3,11,8,12,9,13,5,14,5,15,6,16,6,17,0,18,4,19,1]).reshape(-1,2)


        lines = [Cylinder(radius=0.1, height=np.linalg.norm(coords[bond[j][0],:]-coords[bond[j][1],:]),\
                direction=(coords[bond[j][0],:]-coords[bond[j][1],:])/np.linalg.norm(coords[bond[j][0],:]-coords[bond[j][1],:]))\
                .move_to((coords[bond[j][0],:]+coords[bond[j][1],:])/2)      for j in range(len(bond))]
        spheres = [Sphere(1, fill_opacity=1, resolution=(8,8)).move_to([coords[i,:]]).set_color(RED).scale(0.4) for i in range(len(coords))]
        mol = VGroup(*lines,\
                     *spheres).move_to([0,0,0]).scale(0.5)
        
        lines2 = [Cylinder(radius=0.1, height=np.linalg.norm(coords_[bond[j][0],:]-coords_[bond[j][1],:]),\
                direction=(coords_[bond[j][0],:]-coords_[bond[j][1],:])/np.linalg.norm(coords_[bond[j][0],:]-coords_[bond[j][1],:]))\
                .move_to((coords_[bond[j][0],:]+coords_[bond[j][1],:])/2)      for j in range(len(bond))]
        spheres2 = [Sphere(1, fill_opacity=1, resolution=(8,8)).move_to([coords_[i,:]]).set_color(RED).scale(0.2) for i in range(len(coords))]
        mol_ = VGroup(*lines2,\
                      *spheres2).move_to([0,0,0]).scale(0.9)

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
        plan = Polygon(p1,p2,p3,p4)\
                 .set_opacity(0.4).set_color(BLUE)
        self.play(FadeIn(plan))
        
        self.wait(1)

        self.play(Transform(mol, mol_), run_time=1.5)
        self.wait(1.75)
        self.stop_ambient_camera_rotation("phi")
        self.wait(2)
        

        
        # rmv(self,t1)
        # rmv(self,t2)
        # rmv(self,t3)
        rmv_all(self,[*lines,*spheres, plan])
        self.wait(0.5)
        self.set_camera_orientation(theta=-np.pi/2, phi=0)
        self.wait(0.5)

        ### Slide algo 2 ###
        t1 = Text("Step 2 : Feature", font_size=24).move_to([-5,2,0])
        self.add(t1)
        t2 = Bullet(self,"Let evolve the graph under a laser",[-6,1.5,0])
        t3 = Bullet(self,"Measure an observable, that will be affected by the persistent holomogy",[-6,0.75,0])
        t4 = Bullet(self,"Repeat for different Rydberg radii",[-6,0,0])
        t5 = Bullet(self,"Feed the result as a feature into the prediction model",[-6,-0.75,0])

        self.wait(5)
        
        rmv(self,t1)
        rmv(self,t2)
        rmv(self,t3)
        rmv(self,t4)
        rmv(self,t5)
        rmv(self,Title)
        self.wait(1)

        ### Slide Future ###
        
        Title = Text("Summary", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        self.add(sommaire_sketch)
        self.add(sommaire_text)
        self.wait(1)
        RR = Rectangle(height=4,width=10,fill_color=BLACK, fill_opacity=fill_opacity_black_rectangle, stroke_width=0).move_to([-2,0,0])
        self.play(FadeIn(RR))
        self.wait(1)
        self.play(FadeOut(sommaire_sketch, run_time=0))
        self.play(FadeOut(sommaire_text, run_time=0))
        rmv(self,Title)
        rmv(self,RR)
        self.wait(0.5)

        Title = Text("Project outlook", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        self.wait(1)

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
        
        
        self.play(AnimationGroup(FadeIn(t1),FadeIn(t2), FadeIn(t3), lag_ratio=0.75))
        self.wait(10)

        rmv_all(self,[t1,t2,t3,Title])
        self.wait(1)

        ### Roadmap ###

        Title = Text("Roadmap", font_size=font_title).move_to([0,3.5,0])
        self.add(Title)
        self.wait(1)

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

        textsx = ["Phase 1", "Phase 2", "Phase 3", "Final", "End of POC"]
        labelsx = VGroup(*[Text(textsx[i], font_size=16).move_to([-lx/2+lx*i/nx+lx/nx/2, -ly/2*1.1,0]) for i in range(nx)])

        self.play(AnimationGroup(Write(labelsy),Write(labelsx)))

        arr = [[0.2,3],[0.2,4],[1,7.5],[4,5.25],[5,8]]
        rectangles = VGroup(*[Rectangle(height=ly/(ny+1)*0.8, width=0).move_to([(arr[i][1]+arr[i][0])/2-lx/2,(ny-i)/(ny+1)*ly-ly/2,0]) for i in range(ny)])
        rectangles2 = VGroup(*[Rectangle(height=ly/(ny+1)*0.8, width=arr[i][1]-arr[i][0], fill_opacity=0.5).move_to([(arr[i][1]+arr[i][0])/2-lx/2,(ny-i)/(ny+1)*ly-ly/2,0]) for i in range(ny)])
        rectangles.set_color_by_gradient(BLUE, GREEN, YELLOW)
        rectangles2.set_color_by_gradient(BLUE, GREEN, YELLOW)
        self.play(Transform(rectangles,rectangles2))
        self.wait(1)
        line1 = Line([3*lx/nx-lx/2,-ly/2,0],[3*lx/nx-lx/2,-ly/2,0], color=RED)
        line2 = Line([3*lx/nx-lx/2,-ly/2,0],[3*lx/nx-lx/2,ly/2,0], color=RED)
        self.play(Transform(line1,line2))
        self.wait(1)

        b = Brace(Line([-lx/2,-ly/2*1.2,0],[-lx/2+4*lx/nx,-ly/2*1.2,0]),sharpness=1)
        text_acc = Text("Hackathon ~ 4 weeks",font_size=18).move_to([-lx/2+2*lx/nx,-ly/2*1.5,0])
        text_end = Text("End ~ 6 weeks",font_size=18).move_to([-lx/2+5*lx/nx,-ly/2*1.5,0])
        self.play(FadeIn(b))
        self.play(Write(text_acc))
        self.play(Write(text_end))
        self.wait(8)
        rmv_all(self,[b,text_acc,text_end,rectangles,rectangles2,line2,axes,labelsx,labelsy,Title,line1,line2])

        ### end ###

        self.wait(1)
        self.play(Write(Text("Thank you")))
        self.wait(1)




class Video4(ThreeDScene):
    def construct(self):
        config.disable_caching = True

        self.camera.background_color = BLACK

        # coords = np.array([4.961,1.6677,2.1994,6.5255,3.3354,0.0853,6.3615,2.0653,0.9145,5.5444,3.3354,-1.1217,6.3877,0.0,3.2024,8.2018,3.3354,-0.5982,8.1968,2.7017,-1.0117,9.3435,3.3354,0.3343,9.3579,2.8618,0.8666,6.3615,4.6055,0.9145,8.1968,3.9691,-1.0117,10.6925,3.3354,-0.3343,11.8342,3.3354,0.5982,13.5105,3.3354,-0.0853,13.6745,4.6055,-0.9145,13.6745,2.0653,-0.9145,14.4916,3.3354,1.1217,11.8392,3.9691,1.0117,11.8392,2.7017,1.0117,10.6781,3.809,-0.8666,10.6781,2.8618,-0.8666,9.3579,3.809,0.8666,3.5343,3.3354,1.1965,4.961,5.0031,2.1994,5.4484,3.3354,3.2771,4.4736,0.0,1.1217,5.057,1.6677,-2.1994,5.057,5.0031,-2.1994,4.961,-1.6677,2.1994,15.075,5.0031,-2.1994,15.075,1.6677,-2.1994,14.979,5.0031,2.1994,14.979,1.6677,2.1994,4.4736,6.6708,1.1217,6.3877,6.6708,3.2024]).reshape(-1,3)
        # coords_ = np.array([2.493512197816773,1.1747671198361975,-0.6224315873398683,3.3818473417967443,1.78628047837729,-0.8994301324567181,3.1255774414634017,1.2530061951285887,-0.717354162111515,3.5223802094488224,2.3511995880569483,-1.0772860407828455,2.792045307664153,0.6547490144281605,-0.5078090611052116,3.966248937035289,1.5372303731521437,-0.8951839023201374,3.836209278280183,1.2423818628469874,-0.7958507171994754,4.548590803503691,1.2595734426019607,-0.88251148749126,4.323657303378034,0.7292702884454668,-0.7048816566286399,2.8616003548870648,2.1256951748609025,-0.9369080275768247,4.180425477464021,2.07107307098732,-1.0725928248213576,5.141185864137826,1.0286833488418747,-0.8844044223080967,5.763386921231271,0.9381708931374326,-0.9298831747605201,6.36585792707814,0.7622962390701021,-0.9486596722289652,6.768691703623087,1.1846984426940785,-1.11581083634461,6.299996728373486,0.18421228216510868,-0.775602699681456,6.919752293457124,0.5063054678103911,-0.9389260307328869,6.087668184284849,1.413390537668109,-1.103142303975938,5.689954427948833,0.5624476917010018,-0.8138914445835134,5.386381169672404,1.5462643011351258,-1.0607168444463686,4.990335039881338,0.4716249340483938,-0.7076150965633851,4.677001876735196,1.5658560708697233,-0.9849312867751614,1.8991856734688644,1.4207777640330892,-0.6246688568331855,2.273295737883636,1.9074596533147787,-0.8069268986090204,2.527384184501991,1.5689909458273419,-0.7391806505934867,2.0859409515529155,0.7515059894510397,-0.45449096158851277,3.9082631646166375,2.775122297675716,-1.2429275353368654,3.1861223860829186,2.833971575959366,-1.1769167634430098,2.3867343511396593,0.24874901948599498,-0.34506949294111566,7.202828373798142,1.5619126718775527,-1.2736167880460423,6.379398720090704,-0.3863809113261264,-0.6213578036239926,7.488128773864145,0.6524938354498035,-1.0459941425556152,7.2286460323559965,0.007376862528612225,-0.8315299961779568,1.6896219848576166,2.0850266369606785,-0.7907916889966256,2.2480583151212596,2.494059605640178,-0.9719692502077246]).reshape(-1,3)
        # bond = np.array([0,2,1,2,3,1,4,0,5,1,6,5,7,5,8,7,9,1,10,5,11,7,12,11,13,12,14,13,15,13,16,13,17,12,18,12,19,11,20,11,21,7,22,0,23,9,24,0,25,0,26,3,27,3,28,4,29,14,30,15,31,16,32,16,33,23,34,23,22,23,23,24,25,28]).reshape(-1,2)
        coords = np.array([-0.8275,1.9119,1.7466,-1.0893,-1.6463,-0.6386,-0.7406,-0.1054,0.9215,-1.9138,2.3427,-0.0629,-3.6372,2.6469,-1.4029,0.0916,1.194,3.5778,1.1316,2.1799,0.8475,-1.4887,-0.7217,0.1313,-2.963,-0.4816,0.1188,-3.605,0.6444,-0.1928,-2.9812,1.9585,-0.561,-3.5373,-1.2541,0.3703,-4.6089,0.6003,-0.1747,0.2475,1.6943,4.2199,-0.7254,0.587,4.0592,1.1547,2.7349,0.0559,1.9952,1.4408,0.531,-1.1622,4.0236,2.0904,-3.3025,4.7586,-1.7466,0.8275,-1.9119,-1.7466]).reshape(-1,3)
        coords_ = np.array([0.06985073608313107,0.6362093769414349,0.19521839654512646,-0.5830111410666922,-0.7289925675704391,-0.6151133017428477,-0.19166287035498714,0.1690841732487019,-0.11172026562763296,-0.40686206363229427,0.8617319749833968,-0.12583818956711143,-1.1009912292032182,1.6427997876438771,-0.49309313259798426,0.3849727249752732,0.12236691860591695,0.3266864724329003,0.5259298995406739,0.7863084564063232,0.583381492883584,-0.5641422055815086,-0.143128761596893,-0.4707167534567345,-1.0244171806931848,0.10296953879464536,-0.7744254870637236,-1.181192769470426,0.6859018648312409,-0.7673683532956102,-0.8722970697900717,1.0868387951268357,-0.4382101953136264,-1.4060395155186467,-0.19212644452222724,-1.1367475074877307,-1.6579093148244368,0.8367816412096649,-1.104953985022397,0.8606061066418931,-0.039655572817813164,0.6609622674529562,0.44050867668441224,-0.47199619545531574,0.23831153771394298,0.655285917191794,1.3325416090270739,0.8049869423665147,1.006404247660305,0.6992099414913796,0.9380128559190493,0.03655053453827522,1.2423536603007779,0.30350597991602263,-1.341331693477645,2.192165477674977,-0.5584996550565545,-0.6170000778273629,-1.3108855233552756,-0.7703973973432577]).reshape(-1,3)
        bond = np.array([0,2,1,7,2,7,3,0,4,10,5,0,6,0,7,8,8,9,9,10,10,3,11,8,12,9,13,5,14,5,15,6,16,6,17,0,18,4,19,1]).reshape(-1,2)

        mol = VGroup(*[Line(coords[bond[j][0],:], coords[bond[j][1],:], color=BLUE,stroke_width=10) for j in range(len(bond))],\
                     *[Sphere(1, fill_opacity=1, resolution=(8,8)).move_to([coords[i,:]]).set_color(RED).scale(0.4) for i in range(len(coords))]).move_to([0,0,0]).scale(0.5)
    
        mol_ = VGroup(*[Line(coords_[bond[j][0],:], coords_[bond[j][1],:], color=BLUE,stroke_width=10) for j in range(len(bond))],\
                      *[Sphere(1, fill_opacity=1, resolution=(8,8)).move_to([coords_[i,:]]).set_color(RED).scale(0.2) for i in range(len(coords))]).move_to([0,0,0]).scale(0.9)

        self.set_camera_orientation(theta=0*DEGREES, phi=90*DEGREES)

        self.add(mol)
        self.wait(0.5)

        a = np.array([-0.27364073,  0.96183198,  0.        ])
        b = np.array([-0.74773274, -0.2127296 , -0.62900069])
        p1 = -2*a+2*b
        p2 = -2*a-2*b
        p3 = 2.3*a-2*b
        p4 = p1+p3-p2

        # self.add(Vector(a, color=BLUE))
        # self.add(Vector(b))
        # self.add(Dot(p1,color=BLUE))
        # self.add(Dot(p2,color=WHITE))
        # self.add(Dot(p3,color=GREEN))
        # self.add(Dot(p4,color=RED))


        
        self.begin_ambient_camera_rotation(0.65,"phi")

        self.wait(1)
        self.play(FadeIn(Polygon(p1,p2,p3,p4)\
                 .set_opacity(0.4).set_color(BLUE)))
        
        
        
        # self.move_camera(theta=-90*DEGREES, phi=90*DEGREES)
        # self.move_camera(theta=-170*DEGREES, phi=90*DEGREES)
        # self.move_camera(theta=-170*DEGREES, phi=7  0*DEGREES)
        
        self.wait(1)

        self.play(Transform(mol, mol_), run_time=1.5)
        self.wait(1)
        self.stop_ambient_camera_rotation("phi")
        self.wait(1)
        
