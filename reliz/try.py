import pygame
import sys
import random

# Ініціалізація Pygame
pygame.init()

# Розміри екрану
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Invoker Game")

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифти
font = pygame.font.Font(None, 36)

# Фази гри
PHASE_CONFIGURE_KEYS = 0
PHASE_GAMEPLAY = 1

# Завантаження зображень здібностей
ability_images = {
    'Q': pygame.image.load('icon.webp'),
    'W': pygame.image.load('invoker1.jpg'),
    'E': pygame.image.load('invoker2.jpg')
}

# Масштабування зображень здібностей
for key in ability_images:
    ability_images[key] = pygame.transform.scale(ability_images[key], (50, 50))

# Клас для гравця
class Player:
    def __init__(self):
        self.keys = {'Q': None, 'W': None, 'E': None}
        self.ability_sequence = []
        self.correct_sequence = ['Q', 'W', 'E']  # Приклад правильної послідовності
        self.is_configured = False

    def set_key(self, ability, key):
        self.keys[ability] = key

    def add_ability(self, key):
        for ability, assigned_key in self.keys.items():
            if assigned_key == key:
                self.ability_sequence.append(ability)

    def check_sequence(self):
        return self.ability_sequence == self.correct_sequence

# Основний цикл гри
def main():
    player = Player()
    phase = PHASE_CONFIGURE_KEYS
    ABILITIES = ['Q', 'W', 'E']
    keys_assigned = []
    random.shuffle(ABILITIES)
    current_ability_index = 0
    message = "Press key for ability " + ABILITIES[current_ability_index]

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if phase == PHASE_CONFIGURE_KEYS:
                    if event.key not in keys_assigned:
                        ability = ABILITIES[current_ability_index]
                        player.set_key(ability, event.key)
                        keys_assigned.append(event.key)
                        current_ability_index += 1
                        if current_ability_index < len(ABILITIES):
                            message = "Press key for ability " + ABILITIES[current_ability_index]
                        else:
                            player.is_configured = True
                            phase = PHASE_GAMEPLAY
                            message = "Configuration complete! Press abilities in the correct sequence."

                elif phase == PHASE_GAMEPLAY:
                    player.add_ability(event.key)
                    if player.check_sequence():
                        message = "Correct sequence! Well done!"
                        player.ability_sequence = []
                    else:
                        if len(player.ability_sequence) >= len(player.correct_sequence):
                            message = "Incorrect sequence. Try again."
                            player.ability_sequence = []

        # Очищення екрану
        screen.fill(BLACK)

        # Відображення повідомлення
        text = font.render(message, True, WHITE)
        screen.blit(text, (50, 50))

        # Відображення розкладки клавіш
        if phase == PHASE_GAMEPLAY:
            y_offset = 100
            for ability, key in player.keys.items():
                key_name = pygame.key.name(key)
                key_text = f"Ability {random.choice(ability)}: {key_name.upper()}"
                text = font.render(key_text, True, WHITE)
                screen.blit(text, (50, y_offset))
                y_offset += 40

            # Відображення послідовності здібностей
            sequence_text = "Current Sequence: " + " ".join(player.ability_sequence)
            text = font.render(sequence_text, True, WHITE)
            screen.blit(text, (50, y_offset + 40))

            # Відображення зображень здібностей
            x_offset = 50
            for ability in player.ability_sequence:
                screen.blit(ability_images[ability], (x_offset, y_offset + 80))
                x_offset += 60

        # Оновлення екрану
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
