import pygame, sys
import GameObjects.Button as B
import FontConfig as FC
import GameObjects.Text as T
import GameObject as GO
import Scene as S
import GameObjects.InputField as IF
import Global

WHITE: tuple[int] = (255, 255, 255)
RED: tuple[int]  = (255, 0, 0)
BLUE: tuple[int]  = (0, 0, 255)
BLACK: tuple[int]  = (0, 0, 0)

FORWARD_KEY: int = pygame.K_w
BACKWARD_KEY: int = pygame.K_s
LEFT_KEY: int = pygame.K_a
RIGHT_KEY: int = pygame.K_d

PLAYER_POSITION: list[int] = [100, 100] 

CURRENT_SCENE: S.Scene

def hello() -> None:
    print("hello")
    
def changeScene(objects: list[object]) -> None:
    global CURRENT_SCENE 
    CURRENT_SCENE = objects[0]
    print(CURRENT_SCENE.gameObjects)
    CURRENT_SCENE.draw()
    pygame.display.update()

def main():
    global CURRENT_SCENE
    pygame.init()
    pygame.display.set_caption("Miner Quest")
    Global.GAME_SCREEN = pygame.display.set_mode((640, 480))
    Global.GAME_SCREEN.fill(WHITE)
    pygame.display.update()
    
    basicFontConfig: FC.FontConfig = FC.FontConfig("freesansbold.ttf", BLACK, (RED, BLUE, WHITE), 30)
    basicTextFontConfig: FC.FontConfig = FC.FontConfig("freesansbold.ttf", BLACK, (WHITE, BLUE, WHITE), 30)
    
    sceneTwoText: T.Text = T.Text(100, 100, "This is scene two", basicTextFontConfig)
    sceneTwoButton: B.Button = B.Button(100, 200, basicFontConfig, buttonText="go back to other scene", onClickFunction=changeScene, width=100, height=100)
    sceneTwo: S.Scene = S.Scene([sceneTwoText, sceneTwoButton], backgroundColor=pygame.Color('black'))
    
    b1: B.Button = B.Button(290, 150, basicFontConfig, buttonText="Play", onClickFunction=changeScene, parameters=[sceneTwo])
    b: B.Button = B.Button(290, 250, basicFontConfig, buttonText="Exit", onClickFunction=pygame.QUIT)
    
    # t: T.Text = T.Text(0, 0, "Hello World", basicTextFontConfig)
    t: T.Text = T.Text(0, 0, "Hello World we need some more text here so let me add some here", basicTextFontConfig, width=250)

    i: IF.InputField = IF.InputField(300, 300, basicFontConfig, "Hello World")
    
    gameObjects: GO.GameObject = [t, b, b1]
    scene: S.Scene = S.Scene(gameObjects)
    sceneTwoButton.parameters = [scene]
    
    CURRENT_SCENE = scene
    CURRENT_SCENE.draw()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(CURRENT_SCENE.gameObjects)
                CURRENT_SCENE.processMouseClick()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                print(pygame.key.name(event.key))
                CURRENT_SCENE.processAnyKeyPress(event.key)
                CURRENT_SCENE.draw()
        CURRENT_SCENE.processMouseMovement()

if __name__ == "__main__":
    main()