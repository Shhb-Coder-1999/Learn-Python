import arcade

arcade.open_window(400, 400, "shhb shape")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = column * 20 + 100
        y = row * 20 + 100
        if (row+column)%2==0:
            arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.RED,45)
        else:
            arcade.draw_rectangle_filled(x, y, 10,10, arcade.color.BLUE,45)

arcade.finish_render()
arcade.run()