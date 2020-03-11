# Create Web Macro with Python
- pyautogui 설치
- 키보드, 마우스 제어
- Web 자동화

#### #Setting
- python 설치
  - python.org에서 python 설치 > Python path 체크박스 클릭 후 설치
  - powershell에서 python 입력 시 설치되어있으면 버전 정보 나옴
- pyautogui 설치
  - 시작키+R > powershell > pip install pyautogui


#### #pyauto
- import pyautogui as pag
  - 너무 길어서 pag으로 명명
- pag.기능
  - 마우스
    - .position() > 현재 마우스 커서 x, y 좌표 return
    - .moveTo(x, y) > 해당 좌표로 마우스 이동(절대 좌표)
      - .moveTo(x, y, 2) > 2초 동안 이동
    - .moveRel(x, y) > 현재 마우스 커서 기점으로 마우스 이동(상대 좌표)
      - .moveRel(x, y, 2) > 2초 동안 이동
    - .click(x=x, y=y) OR .click((x, y)) > 해당 좌표 클릭
    - .click(clicks=2, interval=2)) > 2초 간격으로 2번 클릭
    - .rightClick() > 우클릭
    - .doubleClick() > 더블클릭
    - .dragTo(x=x, y=x, duration=2) > 현재 마우스 커서에서부터 해당 좌표까지 드래그. duration(지속): 몇 초 동안 해당 움직임을 수행하겠다.
  - 키보드
    - .typewrite("ABC") > 타이핑
      - .typewrite("ABC", interval=1) > duration과 같은 효과(천천히 타이핑)
      - .typewrite(["enter"]) > enter키 입력 / press와 동일 / press로 정의된 키가 아니면 입력되지 않음
    - .press("enter") > 글자가 아닌 키보드 키 누르기
    - .keyDown("shift") > 해당 키 누르고 있기
    - .keyup("shift") > 해당 키 떼기
    - .hotkey("ctrl","c") > ctrl+c
- import time
  - 다양한 움직임 사이사이 대기 시간을 줘서 원활하게 매크로가 동작하도록 설정
  - time.sleep(1) > 1초 동안 대기
- 참고 링크
  - [pyautoGui 함수](https://m.blog.naver.com/jsk6824/221765884364)
  - [pyautoGui press](https://pyautogui.readthedocs.io/en/latest/keyboard.html)

#### #get image point
- 이미지 파일을 통해 해당 이미지의 좌표를 얻는 것
  - 단순히 좌표로 매크로 만들 시 퓁페이지가 움직이거나 다른 환경에서 적용안되는 것을 이미지를 통해 해결
- opencv 설치
  - pip install opencv-python
  - 잘 모르겠지만 opencv에서 이미지 캡처 라이브러리를 갖고 있는듯
- 기능
  - .locateOnScreen(이미지파일경로) > 해당 이미지와 부함하는 곳의 좌표 return
    - return 값은 (1300, 637, 30, 30)으로 4가지 이며 각각 (x, y, width, height)이다.
    - point = pag.locateOnScreen("7.png") > return 받은 좌표를 변수에 담는다.
    - pag.click(point) 진행 시 click은 x, y좌표를 받기 때문에 파라미터가 달라 실행되지 않음.
  - .center > 자세히 모르겠지만 실질적인 좌표값으로 걸러줌
    - real_point = pag.center(point) > locateOnscreen으로 받은 값의 좌표를 걸러줌
    - pag.click(real_point) 해주면 정상적으로 작동한다.
  - .locateCenterOnScreen(이미지경로) > locateOnScreen, center를 합친 처음부터 좌표를 받는 기능
  - .screenshot(파일명, region=(x, y, width, height)) > 이미지를 캡처해주는 기능
- pyautogui는 아주 엄청나게 빨리 클릭해주지는 않는다. 눈에 보일 정도임

#### #selenium
- 웹 자동화를 위한 크롤링 라이브러리
- pyautogui와 거의 동일, web element에 접근 가능한 점만 다를듯?
- 설치: pip install selenium
- chromedriver 최신버전을 받아서 해당 프로젝트 폴더에 넣어두기
  - 가장 윗 버전, 본인 OS에 맞는 프로그램 다운
  - [다운로드 링크](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- 필요한 라이브러리 import
  ```python
    from selenium import webdriver as wd
    from selenium.webdriver.common.keys import keys
    from selenium.webdriver.common.action_chains import action_chains as ac

    import time
  ```
- Setting
  ```python
    driver = webdriver.Chrome() #크롬 드라이버 사용하겠다.
    URL = "https://www.naver.com" #URL 저장
    driver.get(URL) #해당 URL을 연다. (크롬으로)
    driver.maximize_window() #해당 웹페이지 최대화
    action = ActionChains(driver) #제어할 준비
  ```
- element selector > 아래와 같이 사용
  - driver.find_element_by_css_selector('#id').click() > id
  - driver.find_element_by_css_selector('.lg_local_btn').click() > class
  - driver.find_element_by_css_selector('.class1.class2.class3').click() > 여러개의 class
  - 해당 요소들은 변수에 담아 꺼내쓸 수 있다.
- actionchains
  - .send_keys("ABC") > 해당 내용 입력
  - .key_down(Keys.TAB) > TAB키를 누른다. Keys를 import해야 편하게 사용가능
  - 다 쓴 뒤 .perform() 해줘야지 동작함
- 기능
  - .reset_actions()
    - perform 이후 한번씩 reset해줘서 오류를 방지함
  - .pause(2) > 2초동안 대기
    - time.sleep(2)과 같음
  - action chain은 길게 쭉 붙여서 쓸 수 있고 너무 길어서 가독성이 떨어질 경우 아래와 같이 쓸 수 있다.
    ```python    
      # 한줄로 죽 쓰기
      action.send_keys("asdadsadad").key_down(Keys.TAB).key_down(Keys.TAB).send_keys("ASdasdasdas").key_down(Keys.TAB).send_keys("ASdasdasdas").perform()

      # 백슬래시를 통해 분리
      action.send_keys("asdadsadad").key_down(Keys.TAB)\
          .key_down(Keys.TAB).send_keys("ASdasdasdas").key_down(Keys.TAB)\
          .send_keys("ASdasdasdas").perform()

      # 괄호안에 표기는 다 한줄로 인식
      (
          action.send_keys("asdadsadad").key_down(Keys.TAB)
          .key_down(Keys.TAB).send_keys("ASdasdasdas").key_down(Keys.TAB)
          .send_keys("ASdasdasdas").perform()
      )
    ```
    - .move_to_element(btn).click() > 해당 element 위로 마우스를 이동해서 클릭
      - btn에 버튼 element를 저장해두고 쓸 수 있다.
    - .perform()
      - 잘 모르겠느데 action chains들을 build를 먼저 호출하지 않고 작업 수행
- 참고링크
  - [selenium docs action chains](https://www.selenium.dev/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html)

#### #Selenium2
- 단일 element 접근 method
  - find_element_by_name('HTML_name')
  - find_element_by_id('HTML_id')
  - find_element_by_xpath('/html/body/some/xpath')
  - find_element_by_css_selector('#css > div.selector')
  - find_element_by_class_name('some_class_name')
  - find_element_by_tag_name('h1')
- 여러 elements에 접근하는 method(대부분 element를 elements로 바꾸면 된다)
  - find_elements_by_css_selector('#css > div.selector')
  
#### #실전 테스트(create mecro)
- 첫번째 오류
  - webdriver import가 안되는 오류
  - stackoverflow 답변: 파일이름이 selenium인 것을 지우고, pyc도 지워라.
  - 내 파일 중 selenium.py 파일이 있어서 지웠고, 폴더에 생성된 pyc폴더도 지우니 됨