import pygame,view,model,control,time



while True:
    time.sleep(1/100)
    view.coop()
    control.event()
    model.model()
