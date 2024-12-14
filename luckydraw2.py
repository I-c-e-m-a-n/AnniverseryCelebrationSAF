# Essential imports
import arcade
import random
import math
import arcade.gui
import json
import autoemail as ae          #personal program, remake for distribution
import sheetgetter as sg        #personal program, remake for distribution


# Set constants
# SCREEN_WIDTH = 1440
# SCREEN_HEIGHT = 800

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.window_commands.get_display_size()
SCREEN_TITLE = "46th Anniversary Lucky Draw"
FILE_PATH = 'NS Lucky Draw/testSheet.txt'

# Quit button functionality
class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()

# Main draw function
class MyDraw(arcade.Window): 
    # Initialize drawing
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # Set Main variables
        self.background = arcade.load_texture("NS Lucky Draw/images/luckydrawbackground.png")
        self.scene = 'Menu'
        self.drawbox = None
        self.data = []
        self.sent = 0
        self.picklist = []
        self.done = []

        # Set Helper variables
        self.btn1 = "#"
        self.btn2 = "#"
        self.btn3 = "#"
        self.btn4 = "#"
        self.write = len(self.data)

        self.prizes = ["KONKA 4K ULTRA HD 50 INCH LED SMART TV", 
                       "NINTENDO SWITCH CONSOLE (OLED)",
                       "6KATA FOLDING 20 INCH BIKE",
                       "MIDEA MINI BAR FRIDGE",
                       "NINTENDO SWITCH (LITE)",
                       "AIRPODS THIRD GEN",
                       "VINNFIER HYPERBAR WIRELESS SOUNDBAR",
                       "ARMAGEDDON KEYBOARD",
                       "MAYER HOTPOT W GRILL",
                       "MAGSAFE POWERBANK", #10
                       "EUROPACE AIRFRYER",
                       "SONY HEADPHONES",
                       "BRAUN TOASTER",
                       "POWERPAC RICE COOKER",
                       "POWERPAC VACUUM CLEANER",
                       "BRAUN BATTERY SHAVER",
                       "SONA INDUCTION COOKER",
                       "POWERPAC ELECTRIC OVEN",
                       "CIRCULATOR TABLE FAN",
                       "CORNELL COFFEE MAKER", #20
                       "POWERPAC FOOD STEAMER",
                       "YUAN YANG STEAMBOAT POT",
                       "AUDIOBOX DOCKING SPEAKER",
                       "POWERPAC WAFFLE MAKER",
                       "SKULLCANDY EARPHONES",
                       "ALCATROZ GAMING MOUSE"] #26

        # Set Style variables

        self.start_style = {
            "font_color": arcade.color.SANDSTORM,
            "font_color_pressed": arcade.color.SANDSTORM,
            "border_color": arcade.color.USAFA_BLUE,
            "bg_color": arcade.color.STAR_COMMAND_BLUE,
            "bg_color_pressed": arcade.color.SAPPHIRE_BLUE,
            "border_color_pressed": arcade.color.GOLDENROD,
            "border_width": 4,
            "font_size": 18
        }

        self.quit_style = {
            "border_color_pressed": arcade.color.MAROON,
            "border_color": arcade.color.DARK_SCARLET,
            "bg_color": arcade.color.ROSEWOOD,
            "border_width": 5,
            "font_color": arcade.color.RED,
            "bg_color_pressed": arcade.color.MAROON,
            "font_color_pressed": arcade.color.RED
        }

        self.pick_style = {
            "font_color": arcade.color.GOLDEN_YELLOW,
            "font_size": 20,
            "border_width": 2,
            "bg_color": arcade.color.DARK_LAVENDER,
            "border_color_pressed": arcade.color.GOLDEN_YELLOW,
            "bg_color_pressed": arcade.color.GOLDEN_YELLOW,
            "border_color": arcade.color.OLD_HELIOTROPE
        }

        self.num_style = {
            "border_width": 5,
            "font_color": arcade.color.GOLDEN_YELLOW,
            "font_size": 50,
            "border_color": arcade.color.TOOLBOX,
            "bg_color": arcade.color.RUSSIAN_VIOLET,
            "bg_color_pressed": arcade.color.SAFFRON,  
            "border_color_pressed": arcade.color.SAFFRON
        }

        self.win_style = {
            "border_width": 5,
            "font_color": arcade.color.GOLDEN_YELLOW,
            # "font_size": 50,
            "border_color": arcade.color.TOOLBOX,
            "bg_color": arcade.color.RUSSIAN_VIOLET,
            "bg_color_pressed": arcade.color.SAFFRON,  
            "border_color_pressed": arcade.color.SAFFRON
        }
        
        self.done_style = {
        "font_color": arcade.color.SANDSTORM,
            "font_color_pressed": arcade.color.DIM_GRAY,
            "border_color": arcade.color.DIM_GRAY,
            "bg_color": arcade.color.CHARCOAL,
            "bg_color_pressed": arcade.color.EBONY,
            "border_color_pressed": arcade.color.ASH_GREY,
            "border_width": 4,
            "font_size": 18
        }
        # START 
        self.on_menu()

        # button_style = {
        # "font_size": 20,
        # "font_color": arcade.color.WHITE,
        # "border_width": 2,
        # "border_color": arcade.color.BLACK,
        # "bg_color": arcade.color.BLACK,
        # "bg_color_pressed": arcade.color.WHITE,  
        # "border_color_pressed": arcade.color.BLACK,  
        # "font_color_pressed": arcade.color.WHITE 
        # }
        
        
    # For each tick
    def on_draw(self):
        # background image
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        # Registered persons
        arcade.draw_text(self.write, SCREEN_WIDTH*0.1, SCREEN_HEIGHT*0.95, arcade.color.BLACK, 12, 0, 'left',
                         'calibri', False, False, 'left', 'baseline', False, 0)

        # Set scenes
        # Main menu scene, first scene to load up
        if self.scene == 'Menu':
            # Draw the menu
            self.menu.draw()

        # Lucky Draw pick screen (Lucky Draw 1, Lucky Draw 2, ......)
        if self.scene == 'Draw':
            # Draw the lucky draw picking screen
            self.ldraw.draw()
        
        if self.scene == 'Image':
            # Draw the lucky draw picking screen
            self.imdraw.draw()
        
        # Ticket picking screen
        if self.scene == 'Pick':
            # Draw the ticket picking screen
            self.pdraw.draw()

        # Final number display screen
        if self.scene == 'Num':
            # Draw the boxes with numbers
            self.ndraw.draw()
            if '#' not in self.btn1+self.btn2+self.btn3+self.btn4:
                arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT*0.8, 1030, 300, arcade.color.RUSSIAN_VIOLET)
                arcade.draw_rectangle_outline(SCREEN_WIDTH/2,SCREEN_HEIGHT*0.8, 1030, 300, arcade.color.TOOLBOX, 5)
                
                arcade.draw_text("CONGRATULATIONS",
                                  SCREEN_WIDTH*0.15, SCREEN_HEIGHT*0.8775, arcade.color.GOLDEN_YELLOW, 75, 0, 'left',
                         'calibri', False, False, 'left', 'baseline', False, 0)
                arcade.draw_text("Presenting the winner of:",
                                  SCREEN_WIDTH*0.15, SCREEN_HEIGHT*0.83125, arcade.color.GOLDEN_YELLOW, 30, 0, 'left',
                         'calibri', False, False, 'left', 'baseline', False, 0)
                arcade.draw_text(self.prizes[int(self.drawbox)-1],
                                  SCREEN_WIDTH*0.15, SCREEN_HEIGHT*0.77875, arcade.color.GOLDEN_YELLOW, 30, 0, 'left',
                         'calibri', False, False, 'left', 'baseline', False, 0)
                try:
                    arcade.draw_text(self.data[int(self.btn2+self.btn3+self.btn4)][1],
                                    SCREEN_WIDTH*0.15, SCREEN_HEIGHT*0.7, arcade.color.GOLDEN_YELLOW, 30, 0, 'left',
                            'calibri', False, False, 'left', 'baseline', False, 0)

                    arcade.draw_text("From "+ self.data[int(self.btn2+self.btn3+self.btn4)][4],
                                    SCREEN_WIDTH*0.15, SCREEN_HEIGHT*0.64375, arcade.color.GOLDEN_YELLOW, 30, 0, 'left',
                            'calibri', False, False, 'left', 'baseline', False, 0)
                except:
                    arcade.draw_text(self.btn1+self.btn2+self.btn3+self.btn4,
                                    SCREEN_WIDTH*0.22, SCREEN_HEIGHT*0.65, arcade.color.GOLDEN_YELLOW, 30, 0, 'left',
                            'calibri', False, False, 'left', 'baseline', False, 0)

    # Main Menu
    def on_menu(self):
        self.write = len(self.data) - len(self.picklist)

        self.background = arcade.load_texture("NS Lucky Draw/images/luckydrawbackground.png")
        self.drawbox = None

        # Main gui for menu
        self.menu = arcade.gui.UIManager()
        self.menu.enable()

        # Container for buttons
        self.v_box = arcade.gui.UIBoxLayout()

        # Create the buttons
        self.start_button = arcade.gui.UIFlatButton(text="Start Lucky Draw", height=75, width=300, style=self.start_style)
        self.v_box.add(self.start_button.with_space_around(bottom=20))
        if not self.write:
            self.start_button._style = self.done_style

        self.mail_button = arcade.gui.UIFlatButton(text="Send Mail", height=75, width=300, style=self.start_style)
        self.v_box.add(self.mail_button.with_space_around(bottom=20))

        # Special quit, calling the class
        quit_button = QuitButton(text="Quit", height=75, width=300, style=self.quit_style)
        self.v_box.add(quit_button)

        self.start_button.on_click = self.on_click_start
        self.mail_button.on_click = self.on_click_mail

        self.menu.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_image(self):
        if self.drawbox:
            try:
                self.background = arcade.load_texture("NS Lucky Draw/images/test" + self.drawbox + ".png")
            except:
                pass

        # Main gui for image 
        self.imdraw = arcade.gui.UIManager()
        self.imdraw.enable()

        # Container for buttons
        self.imv_box = arcade.gui.UIBoxLayout()

        next_button = arcade.gui.UIFlatButton(text="Start Lucky Draw", height=50, width=210, style=self.start_style)
        self.imv_box.add(next_button.with_space_around(bottom=20))

        next_button.on_click = self.on_click_image

        self.imdraw.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-350,
                child=self.imv_box)
        )


    # Lucky Draw pick screen (Lucky Draw 1, Lucky Draw 2, ......)
    def on_lucky_draw(self):
        # Main gui for lucky draw
        self.ldraw = arcade.gui.UIManager()
        self.ldraw.enable()

        # Containers for buttons
        self.v_box0 = arcade.gui.UIBoxLayout()
        self.v_box0.vertical = False
        self.v_box0._space_between = 10

        self.v_box1 = arcade.gui.UIBoxLayout()
        self.v_box1.vertical = False
        self.v_box1._space_between = 10

        self.v_box2 = arcade.gui.UIBoxLayout()
        self.v_box2.vertical = False
        self.v_box2._space_between = 10

        self.v_box3 = arcade.gui.UIBoxLayout()
        self.v_box3.vertical = False
        self.v_box3._space_between = 10

        self.v_box4 = arcade.gui.UIBoxLayout()
        self.v_box4.vertical = False
        self.v_box4._space_between = 10

        self.v_box5 = arcade.gui.UIBoxLayout()
        self.v_box5.vertical = False
        self.v_box5._space_between = 10

        self.v_box6 = arcade.gui.UIBoxLayout()
        self.v_box6.vertical = False
        self.v_box6._space_between = 10

        # Buttons
        self.draw_buttons = []

        # 1
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 1", height=70,
                                                         width=220, style=self.start_style))
        self.v_box0.add(self.draw_buttons[0])
        self.draw_buttons[0].on_click = self.on_click_draw1

        # 2 - 6
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 2", width=250, style=self.start_style))
        self.v_box1.add(self.draw_buttons[1])
        self.draw_buttons[1].on_click = self.on_click_draw2

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 3", width=250, style=self.start_style))
        self.v_box1.add(self.draw_buttons[2])
        self.draw_buttons[2].on_click = self.on_click_draw3

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 4", width=250, style=self.start_style))
        self.v_box1.add(self.draw_buttons[3])
        self.draw_buttons[3].on_click = self.on_click_draw4

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 5", width=250, style=self.start_style))
        self.v_box1.add(self.draw_buttons[4])
        self.draw_buttons[4].on_click = self.on_click_draw5

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 6", width=200, style=self.start_style))
        self.v_box2.add(self.draw_buttons[5])
        self.draw_buttons[5].on_click = self.on_click_draw6

        # 7 - 11
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 7", width=200, style=self.start_style))
        self.v_box2.add(self.draw_buttons[6])
        self.draw_buttons[6].on_click = self.on_click_draw7

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 8", width=200, style=self.start_style))
        self.v_box2.add(self.draw_buttons[7])
        self.draw_buttons[7].on_click = self.on_click_draw8

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 9", width=200, style=self.start_style))
        self.v_box2.add(self.draw_buttons[8])
        self.draw_buttons[8].on_click = self.on_click_draw9

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 10", width=200, style=self.start_style))
        self.v_box2.add(self.draw_buttons[9])
        self.draw_buttons[9].on_click = self.on_click_draw10

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 11", width=200, style=self.start_style))
        self.v_box3.add(self.draw_buttons[10])
        self.draw_buttons[10].on_click = self.on_click_draw11

        # 11 - 15
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 12", width=200, style=self.start_style))
        self.v_box3.add(self.draw_buttons[11])
        self.draw_buttons[11].on_click = self.on_click_draw12

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 13", width=200, style=self.start_style))
        self.v_box3.add(self.draw_buttons[12])
        self.draw_buttons[12].on_click = self.on_click_draw13

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 14", width=200, style=self.start_style))
        self.v_box3.add(self.draw_buttons[13])
        self.draw_buttons[13].on_click = self.on_click_draw14

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 15", width=200, style=self.start_style))
        self.v_box3.add(self.draw_buttons[14])
        self.draw_buttons[14].on_click = self.on_click_draw15

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 16", width=200, style=self.start_style))
        self.v_box4.add(self.draw_buttons[15])
        self.draw_buttons[15].on_click = self.on_click_draw16

        # 16 - 20
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 17", width=200, style=self.start_style))
        self.v_box4.add(self.draw_buttons[16])
        self.draw_buttons[16].on_click = self.on_click_draw17

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 18", width=200, style=self.start_style))
        self.v_box4.add(self.draw_buttons[17])
        self.draw_buttons[17].on_click = self.on_click_draw18

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 19", width=200, style=self.start_style))
        self.v_box4.add(self.draw_buttons[18])
        self.draw_buttons[18].on_click = self.on_click_draw19

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 20", width=200, style=self.start_style))
        self.v_box4.add(self.draw_buttons[19])
        self.draw_buttons[19].on_click = self.on_click_draw20

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 21", width=200, style=self.start_style))
        self.v_box5.add(self.draw_buttons[20])
        self.draw_buttons[20].on_click = self.on_click_draw21

        # 21 - 25
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 22", width=200, style=self.start_style))
        self.v_box5.add(self.draw_buttons[21])
        self.draw_buttons[21].on_click = self.on_click_draw22
        
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 23", width=200, style=self.start_style))
        self.v_box5.add(self.draw_buttons[22])
        self.draw_buttons[22].on_click = self.on_click_draw23

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 24", width=200, style=self.start_style))
        self.v_box5.add(self.draw_buttons[23])
        self.draw_buttons[23].on_click = self.on_click_draw24

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 25", width=200, style=self.start_style))
        self.v_box5.add(self.draw_buttons[24])
        self.draw_buttons[24].on_click = self.on_click_draw25

        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Lucky Draw 26", width=200, style=self.start_style))
        self.v_box5.add(self.draw_buttons[25])
        self.draw_buttons[25].on_click = self.on_click_draw26

        # Quit button
        self.draw_buttons.append(arcade.gui.UIFlatButton(text="Quit Lucky Draw ", width=200, style=self.quit_style))
        self.v_box6.add(self.draw_buttons[26])
        self.draw_buttons[26].on_click = self.on_click_draw_quit

        for i in self.done:
            self.draw_buttons[int(i)-1]._style = self.done_style
            

        # Add button containers to GUI
        self.ldraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=300,
                child=self.v_box0))
        self.ldraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=200,
                child=self.v_box1))
        self.ldraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=100,
                child=self.v_box2))
        self.ldraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box3))
        self.ldraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-100,
                child=self.v_box4))
        self.ldraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-200,
                child=self.v_box5))
        self.ldraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-300,
                child=self.v_box6))

    # Ticket picking screen
    def on_pick_screen(self):
        # Main Ticket picking gui
        self.pdraw = arcade.gui.UIManager()
        self.pdraw.enable()
        self.datalen = len(self.data)
        # self.datalen = 433
        # Holds the buttons in an array
        self.draw_ppl = []

        # Button containers
        # draw 1
        self.v_boxp = arcade.gui.UIBoxLayout()
        self.v_boxp.vertical = False
        self.v_boxp._space_between = 10
        # draw 2
        self.v_boxp1 = arcade.gui.UIBoxLayout()
        self.v_boxp1.vertical = False
        self.v_boxp1._space_between = 10
        # draw 3
        self.v_boxp2 = arcade.gui.UIBoxLayout()
        self.v_boxp2.vertical = False
        self.v_boxp2._space_between = 10
        # draw 4
        self.v_boxp3 = arcade.gui.UIBoxLayout()
        self.v_boxp3.vertical = False
        self.v_boxp3._space_between = 10
        # draw 5
        self.v_boxp4 = arcade.gui.UIBoxLayout()
        self.v_boxp4.vertical = False
        self.v_boxp4._space_between = 10
        # draw 6
        self.v_boxp5 = arcade.gui.UIBoxLayout()
        self.v_boxp5.vertical = False
        self.v_boxp5._space_between = 10
        # draw 7
        self.v_boxp6 = arcade.gui.UIBoxLayout()
        self.v_boxp6.vertical = False
        self.v_boxp6._space_between = 10
        # draw 8
        self.v_boxp7 = arcade.gui.UIBoxLayout()
        self.v_boxp7.vertical = False
        self.v_boxp7._space_between = 10
        # draw 9
        self.v_boxp8 = arcade.gui.UIBoxLayout()
        self.v_boxp8.vertical = False
        self.v_boxp8._space_between = 10
        # draw 10
        self.v_boxp9 = arcade.gui.UIBoxLayout()
        self.v_boxp9.vertical = False
        self.v_boxp9._space_between = 10
        # draw 11
        self.v_boxp10 = arcade.gui.UIBoxLayout()
        self.v_boxp10.vertical = False
        self.v_boxp10._space_between = 10
        # draw 12
        self.v_boxp11 = arcade.gui.UIBoxLayout()
        self.v_boxp11.vertical = False
        self.v_boxp11._space_between = 10
        # draw 13
        self.v_boxp12 = arcade.gui.UIBoxLayout()
        self.v_boxp12.vertical = False
        self.v_boxp12._space_between = 10
        # draw quit
        self.v_boxpq = arcade.gui.UIBoxLayout()
        self.v_boxpq.vertical = False
        self.v_boxpq._space_between = 10

        # quit button
        quit = arcade.gui.UIFlatButton(text="Quit", width=200, height=50, style=self.quit_style)
        quit.on_click = self.on_click_pickq
        self.v_boxpq.add(quit)

        # For the number of people registered, add as many buttons to the button array
        for j in range(self.datalen):
            self.draw_ppl.append(arcade.gui.UIFlatButton(text='*', width=25, height=45, style=self.pick_style))
            # self.draw_ppl.append(arcade.gui.UIFlatButton(width=25, height=45, style=self.pick_style))

        # If people have registered
        if self.datalen:
            # Store number of people
            temp = self.datalen - len(self.picklist)

            # Range 40 as for the set width and height (25, 45), the rows neatly hold 40 tickets
            # draw 1
            for i in range(34):
                # If every person is accounted for
                if not temp:
                    # stop adding tickets
                    break
                # Else account for one person and add their ticket to their box
                temp -=1
                self.v_boxp.add(self.draw_ppl[i])
                self.draw_ppl[i].on_click = self.on_click_pick
            # draw 2
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp1.add(self.draw_ppl[i+34])
                self.draw_ppl[i+34].on_click = self.on_click_pick
            # draw 3
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp2.add(self.draw_ppl[i+34*2])
                self.draw_ppl[i+34*2].on_click = self.on_click_pick
            # draw 4
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp3.add(self.draw_ppl[i+34*3])
                self.draw_ppl[i+34*3].on_click = self.on_click_pick
            # draw 5
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp4.add(self.draw_ppl[i+34*4])
                self.draw_ppl[i+34*4].on_click = self.on_click_pick
            # draw 6
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp5.add(self.draw_ppl[i+34*5])
                self.draw_ppl[i+34*5].on_click = self.on_click_pick
            # draw 7
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp6.add(self.draw_ppl[i+34*6])
                self.draw_ppl[i+34*6].on_click = self.on_click_pick
            # draw 8
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp7.add(self.draw_ppl[i+34*7])
                self.draw_ppl[i+34*7].on_click = self.on_click_pick
            # draw 9
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp8.add(self.draw_ppl[i+34*8])
                self.draw_ppl[i+34*8].on_click = self.on_click_pick
            # draw 10
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp9.add(self.draw_ppl[i+34*9])
                self.draw_ppl[i+34*9].on_click = self.on_click_pick
            # draw 11
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp10.add(self.draw_ppl[i+34*10])
                self.draw_ppl[i+34*10].on_click = self.on_click_pick
            # draw 12
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp11.add(self.draw_ppl[i+34*11])
                self.draw_ppl[i+34*11].on_click = self.on_click_pick
            # draw 13
            for i in range(34):
                if not temp:
                    break
                temp -=1
                self.v_boxp12.add(self.draw_ppl[i+34*12])
                self.draw_ppl[i+34*12].on_click = self.on_click_pick
            

        # Add all the button containers to the main gui
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=310,
                child=self.v_boxp))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=260,
                child=self.v_boxp1))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=210,
                child=self.v_boxp2))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=160,
                child=self.v_boxp3))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=110,
                child=self.v_boxp4))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=60,
                child=self.v_boxp5))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=10,
                child=self.v_boxp6))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-40,
                child=self.v_boxp7))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-90,
                child=self.v_boxp8))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-140,
                child=self.v_boxp9))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-190,
                child=self.v_boxp10))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-240,
                child=self.v_boxp11))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-290,
                child=self.v_boxp12))
        self.pdraw.add(arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-350,
                child=self.v_boxpq))
       
    # Numbers display screen  
    def on_number_screen(self):
        # Main number display GUI
        self.ndraw = arcade.gui.UIManager()
        self.ndraw.enable()

        # Button container
        self.v_numbox = arcade.gui.UIBoxLayout()
        self.v_numbox.vertical = False
        self.v_numbox._space_between = 10

        # Quit button container
        self.v_numq = arcade.gui.UIBoxLayout()
        self.v_numq.vertical = False
        self.v_numq._space_between = 10

        # Create the buttons
        button1 = arcade.gui.UIFlatButton(text=self.btn1, width=200, height=150, style=self.num_style)
        button2 = arcade.gui.UIFlatButton(text=self.btn2, width=200, height=150, style=self.num_style)
        button3 = arcade.gui.UIFlatButton(text=self.btn3, width=200, height=150, style=self.num_style)
        button4 = arcade.gui.UIFlatButton(text=self.btn4, width=200, height=150, style=self.num_style)

        button1.on_click = self.on_click_num1
        button2.on_click = self.on_click_num2
        button3.on_click = self.on_click_num3
        button4.on_click = self.on_click_num4

        # Add to their containers
        self.v_numbox.add(button1.with_space_around(bottom=20))
        self.v_numbox.add(button2.with_space_around(bottom=20))
        self.v_numbox.add(button3.with_space_around(bottom=20))
        self.v_numbox.add(button4.with_space_around(bottom=20))

        # Add win button to it's container
        win_button = QuitButton(text="Notify Winner", width=200, style=self.win_style)
        win_button.on_click = self.on_click_win
        self.v_numq.add(win_button)

        # Add quit button to it's container
        quit_button = QuitButton(text="Quit Draw", width=200, style=self.quit_style)
        quit_button.on_click = self.on_click_pickq
        self.v_numq.add(quit_button)

        # Add containers to the gui
        self.ndraw.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_numbox)
        )
        self.ndraw.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                # anchor_y="center_y",
                align_y=-200,
                child=self.v_numq)
        )


# CLICK EVENTS
    # MENU EVENTS
    def on_click_start(self, event):
        if self.write:
            self.on_lucky_draw()
            print("Start: Lucky Draw")
            self.scene = 'Draw'
            self.menu.disable()
    
    def on_click_mail(self, event):
        self.menu.disable()
        print("Sending E-Mails, please wait")
        self.data_mail()
        print("Sent E-Mails")
        self.start_button._style = self.start_style
        self.menu.enable()
        self.write = len(self.data) - len(self.picklist)


    # PICK SCREEN EVENTS
    def on_click_pick(self, event):
        list = [1129, 1019, 1072, 1027, 1257, 1237, 1135, 1032, 1019, 1331, 1320, 1144, 1119, 1076, 1330, 1013, 1274, 1192, 1191]
        for i in list:
            if i not in self.picklist:
                self.picklist.append(i)
        # print("Lucky Draw number = ", self.drawbox)
        try:
            self.background = arcade.load_texture("NS Lucky Draw/images/luckydrawbackground.png")
        except:
            pass
        self.on_number_screen()
        # self.get_data()
        num = str(random.randint(1000, 1000+self.sent-1))
        while num in self.picklist:
            num = str(random.randint(1000, 1000+self.sent-1))
        self.picklist.append(num)
        # self.dump_data(num)
        self.scene = 'Num'
        self.pdraw.disable()
        print("Start: Number Screen, lucky number is ", num)
    

    # NUMBER SCREEN EVENTS
    def on_click_num1(self, event):
        self.btn1 = self.picklist[-1][0]
        self.on_number_screen()
    def on_click_num2(self, event):
        self.btn2 = self.picklist[-1][1]
        self.on_number_screen()
    def on_click_num3(self, event):
        self.btn3 = self.picklist[-1][2]
        self.on_number_screen()
    def on_click_num4(self, event):
        self.btn4 = self.picklist[-1][3]
        self.on_number_screen()

    def on_click_win(self, event):
        # ae.sendWinMail(self.data[int(self.btn2+self.btn3+self.btn4)][3], 
        #                          self.data[int(self.btn2+self.btn3+self.btn4)][2], 
        #                          self.data[int(self.btn2+self.btn3+self.btn4)][1], 
        #                          self.prizes[int(self.drawbox)-1])
        self.done.append(self.drawbox)


    # IMAGE SCREEN EVENTS
    def on_click_image(self, event):
        try:
            self.background = arcade.load_texture("NS Lucky Draw/images/luckydrawbackground.png")
        except:
            pass
        self.on_pick_screen()
        self.scene = 'Pick'
        self.imdraw.disable()
        print("Start: Pick")

    # LUCKY DRAW EVENTS
    def on_click_draw1(self, event):
        self.drawbox = '1'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw2(self, event):
        self.drawbox = '2'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw3(self, event):
        self.drawbox = '3'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw4(self, event):
        self.drawbox = '4'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw5(self, event):
        self.drawbox = '5'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw6(self, event):
        self.drawbox = '6'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw7(self, event):
        self.drawbox = '7'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw8(self, event):
        self.drawbox = '8'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw9(self, event):
        self.drawbox = '9'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw10(self, event):
        self.drawbox = '10'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw11(self, event):
        self.drawbox = '11'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw12(self, event):
        self.drawbox = '12'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw13(self, event):
        self.drawbox = '13'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw14(self, event):
        self.drawbox = '14'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw15(self, event):
        self.drawbox = '15'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw16(self, event):
        self.drawbox = '16'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw17(self, event):
        self.drawbox = '17'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw18(self, event):
        self.drawbox = '18'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw19(self, event):
        self.drawbox = '19'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw20(self, event):
        self.drawbox = '20'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw21(self, event):
        self.drawbox = '21'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw22(self, event):
        self.drawbox = '22'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw23(self, event):
        self.drawbox = '23'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw24(self, event):
        self.drawbox = '24'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw25(self, event):
        self.drawbox = '25'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")
    def on_click_draw26(self, event):
        self.drawbox = '26'
        if self.drawbox not in self.done:
            self.on_image()
            self.scene = 'Image'
            self.ldraw.disable()
            print("Start: image")

    # QUIT EVENTS
    def on_click_draw_quit(self, event):
        self.on_menu()
        self.drawbox = None
        self.scene = 'Menu'
        self.ldraw.disable()
        print("Start: Menu")
    
    def on_click_pickq(self, event):
        self.btn1 = "#"
        self.btn2 = "#"
        self.btn3 = "#"
        self.btn4 = "#"
        self.on_menu()
        self.scene = 'Menu'
        self.pdraw.disable()
        print("Start: Menu")


    # HELP FUNCTIONS
    # def dump_data(self, number):
    #     with open('NS Lucky Draw/drawn.txt', 'w') as f:
    #         for item in self.picklist:
    #             print(item)
    #             f.write("[%s]\n" % str(item))
    #         f.write("[%s]\n" % str(number))

    # def get_data(self):
    #     with open('NS Lucky Draw/drawn.txt', 'r') as file:
    #         lines = file.readlines()
    #         print(lines)
    #         for item in lines:
    #             self.picklist.append(item)
                    
    
    def data_mail(self):
        sg.do_all()
        mail_list = []
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        for line in lines:
            try:
                line_data = json.loads(line.strip())
                if line_data not in self.data:
                    self.data.append(line_data)
                    mail_list.append(line_data)
            except json.JSONDecodeError as e:
                # print(f"Error decoding line '{line.strip()}': {e}")
                pass
        # self.sent = ae.send_bulk_mail(mail_list)   ###########
        for i in mail_list:
        #     # ae.sendMail(i[3], i[1], 1000 + self.sent)
            self.sent += 1
            # print("Mails sent = ", self.sent)
        print("Mails sent = ", self.sent)
        return



# For future additional functionality
    # def on_mouse_press(self, x, y, button, modifiers):
    #     pass
    # def on_update(self, delta_time):
    #     pass
    # def on_key_press(self, key, modifiers):
    #     pass
    # def on_key_release(self, key, modifiers):
    #     pass


def main():
    MyDraw(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()