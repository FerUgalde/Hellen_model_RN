import os

import cv2


#               CREAR CARPETAS PARA ALMACENAR ENTRENAMIENTO y VALIDACION
direccion = 'C:/Users/ferug/Documents/Ing. Software/6to Semestre/Interaccion Humano Computadora/Hellen/Dataset'

# En caso de no existir la carpeta, se crea una
if not os.path.exists(direccion):
    print("Se ha creado la carpeta: ", direccion)
    os.makedirs(direccion)

number_of_classes = 14           #[0 ,...,9, 'inicio_h', 'clima_c', 'foco_l', 'alarma_a']
dataset_size = 800

cap = cv2.VideoCapture(0)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(direccion, str(j))):
        os.makedirs(os.path.join(direccion, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 200
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(direccion, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()