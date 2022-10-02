import cv2

url = 'sweden.mp4'

rastreador = cv2.TrackerCSRT_create()


video = cv2.VideoCapture(url)


ok, frame = video.read()     # ok retorna True enquanto o video estiver ativo, frame retorna cada frame do video


bbox = cv2.selectROI(frame)   # Seleciona a area de interesse


ok = rastreador.init(frame, bbox)    # Retorna true se o frame bbox foi encontrado no frame do video

while True:
    ok, frame = video.read()         # roda o video, salvando cada frame dele

    if not ok:              # no momento que o video acaba acabam os frames ent o while acaba também
        break 

    ok, bbox = rastreador.update(frame)              # atualizamos o bbox com o nome frame

    if ok:
        (x, y, w, h) = [int(v) for v in bbox]         # retornamos o nosso bbox posição x e y, nossa largura e altura
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,200,0),2,1)

    else:
        cv2.putText(frame, 'falha', (100,20), cv2.FONT_HERSHEY_COMPLEX, .75, (0,0,255),2)

    cv2.imshow('Rastreando',frame)
    
    if cv2.waitKey(1) & 0XFF == 27:
        break
