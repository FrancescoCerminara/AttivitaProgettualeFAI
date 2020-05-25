from naoqi import  ALProxy

ip="127.0.0.1"
porta=9559


motion= ALProxy("ALMotion",ip,porta)
movimenti= ALProxy("ALPosture",ip,porta)
motion.moveInit()
motion.wakeUp()

movimenti.goToPosture("StandInt",1.0)
movimenti.goToPosture("Sit",1.0)
movimenti.goToPosture("Crouch",1.0)
movimenti.goToPosture("Stand",1.0)




motion.rest()
