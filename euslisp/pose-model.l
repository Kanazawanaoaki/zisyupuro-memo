(defclass 2d-pose-model
  :super cascaded-link
  :slots (end-coords torso larm1 larm2 rarm1 rarm2 lleg1 lleg2 rleg1 rleg2))
(defmethod 2d-pose-model
  (:init ()
   (let (b1 b2 b3)
     (send-super :init)

     (setq b1 (make-cube 10 10 150))
     (send b1 :locate #f(0 0 75))
     (setq b2 (make-cube 30 10 10))
     (send b2 :locate #f(0 0 125))
     (setq b1 (body+ b1 b2))

     (objects b1)

     )))

(setq r (instance 2d-pose-model))
