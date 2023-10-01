from pico2d import *

# test size 800, 600
TUK_WIDTH, TUK_HEIGHT = 800, 600
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
    print(hand_point_list)

def character_move_to_hand(hand_point):
    # move character
    # if meet hand:
    # list[0] delete and move to new list[0]
    pass

def draw_all_hand():
    global hand, hand_point_list
    for point in hand_point_list[1::]:
        hand.draw(*point)


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

# store clicked point in list
hand_point_list = [[]]

while running:
    clear_canvas()

    # character move
    # character_move_to_hand()

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)

    # created hands draw
    draw_all_hand()

    update_canvas()
    frame = (frame + 1) % 8

    handle_events()

close_canvas()