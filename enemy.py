import pygame

def load_image(name):
    reqname = os.path.join('data', name)
    try:
        picture = pygame.image.load(reqname)
    except pygame.error, message:
        Print "cannot load this image:", name
        raise SystemExit, message
    image = image.convert()
    return picture, picture.get_rect()
class Enemy(sprite.Sprite):

	def_init_(self):
		sprite.Sprite._init_(self)
		self.image, self.box = load_image(enemy_image)
		screen = display.get_surface()
		self.block = screen.get_rect()
		self.speed = 5

	def_update_(self):
		new_x, new_y
		t = random.randint(0,3)
		nextspot = self.box
		if t == 0
			new_x = self.speed
			new_y = 0
		if t == 1
			new_x = -self.speed
			new_y = 0
		if t == 2
			new_x = 0
			new_y = self.speed
		if t == 3
			new_x = 0
			new_y = -self.speed
		nextspot = self.box.move(new_x, new_y)
		if not self.block.contains(nextspot):
		if self.box.left < self.block.left or self.box.right > self.block.right or \
				self.box.top > self.block.top or \
					self.box.bottom < self.block.bottom:
			new_x = -new_x
			new_y = -new_y
		nextspot = self.box.move(new_x, new_y)
		self.box = nextspot
	