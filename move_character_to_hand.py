from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def handle_events():
    global running 

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            create_hand_click_point((event.x, TUK_HEIGHT -  1 - event.y))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    # if mouse click: call create_hand_click_point

def create_hand_click_point(point):
    hand_point_list.append([*point])

def character_move_to_hand():
    global hand_point_list

    if len(hand_point_list) > 0:
        hand_point = hand_point_list[0]
        global x, y, speed, flip
        move_speed = speed / 100

        x = (1 - move_speed) * x + move_speed * hand_point[0]
        y = (1 - move_speed) * y + move_speed * hand_point[1]
        if round(x) == hand_point[0] and round(y) == hand_point[1]:
            del hand_point_list[0]

def draw_all_hand():
    global hand, hand_point_list
    for point in hand_point_list:
        hand.draw(*point)


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
speed = 5

# store clicked point in list
hand_point_list = []

while running:
    clear_canvas()

    # character move
    character_move_to_hand()


    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)


    # created hands draw
    draw_all_hand()
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

    delay(0.001)

close_canvas()