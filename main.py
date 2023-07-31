import pygame,model,view,control,time



while True:
    time.sleep(1/100)
    view.coop()
    control.event()
    model.model()
