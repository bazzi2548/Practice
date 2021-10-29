import pygame

pygame.init() # 초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# FPS
clock = pygame.time.Clock()


# 배경 이미지 불러오기
background = pygame.image.load("D:/Edu/pygame_basic/background.png")


# 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)

# 총 시간
total_time = 100

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작  tick을 받아옴

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임수


    screen.blit(background, (0, 0)) # 배경 그리기
    
    # 타이머 집어 넣기

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,255,255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10,10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time-elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임화면을 다시 그리기!

    # 잠시 대기


# pygame 종료
pygame.quit()