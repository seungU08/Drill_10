#게임 월드 관리 모듈

#게임 월드의 표현
#두개의 layer를 갖는 게임월드구현

objects = [ [], []]

def add(o, depth=0):
    objects[depth].append(o)

def update():
    for layer in objects:
        for o in layer:
            o.update()

def render():
    for layer in objects:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            return
    raise ValueError('?')


