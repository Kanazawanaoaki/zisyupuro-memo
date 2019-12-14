(defclass 2d-pose-model
  :super cascaded-link
  :slots (torso larm1 larm2 rarm1 rarm2 lleg1 lleg2 rleg1 rleg2 j1 j2 j3 j4 j5 j6 j7 j8))
(defmethod 2d-pose-model
  (:init ()
   (let (b1 b2 b3)
     (send-super :init)

     ;;胴体
     (setq b1 (make-cube 10 10 150))
     (send b1 :locate #f(0 0 75))
     (setq b2 (make-cube 40 10 10))
     (send b2 :locate #f(0 0 125))
     (setq b1 (body+ b1 b2))
     (send b1 :set-color :yellow)
     (setq torso (instance bodyset-link :init (make-cascoords) :bodies (list b1) :name 'torso))

     ;;右上腕
     (setq b1 (make-cube 60 10 10))
     (send b1 :locate #f(0 0 5))
     (send b1 :set-color :orange)
     (setq rarm1 (instance bodyset-link :init (make-cascoords :pos #f(-30 0 5)) :bodies (list b1) :name 'rarm1))
     (send rarm1 :locate #f(50 0 120))
     (send torso :assoc rarm1)

     ;;右下腕
     (setq b1 (make-cube 60 10 10))
     (send b1 :locate #f(0 0 5))
     (send b1 :set-color :red)
     (setq rarm2 (instance bodyset-link :init (make-cascoords :pos #f(-30 0 5)) :bodies (list b1) :name 'rarm2))
     (send rarm2 :locate #f(110 0 120))
     (send rarm1 :assoc rarm2)

     ;;左上腕
     (setq b1 (make-cube 60 10 10))
     (send b1 :locate #f(0 0 5))
     (send b1 :set-color :orange)
     (setq larm1 (instance bodyset-link :init (make-cascoords :pos #f(30 0 5)) :bodies (list b1) :name 'larm1))
     (send larm1 :locate #f(-50 0 120))
     (send torso :assoc larm1)

     ;;左下腕
     (setq b1 (make-cube 60 10 10))
     (send b1 :locate #f(0 0 5))
     (send b1 :set-color :red)
     (setq larm2 (instance bodyset-link :init (make-cascoords :pos #f(30 0 5)) :bodies (list b1) :name 'larm2))
     (send larm2 :locate #f(-110 0 120))
     (send larm1 :assoc larm2)

     ;;右もも
     (setq b1 (make-cube 80 10 10))
     (send b1 :locate #f(0 0 0))
     (send b1 :set-color :green)
     (setq rleg1 (instance bodyset-link :init (make-cascoords :pos #f(-40 0 5)) :bodies (list b1) :name 'rleg1))
     (send rleg1 :locate #f(40 0 0))
     (send torso :assoc rleg1)

     ;;右すね
     (setq b1 (make-cube 80 10 10))
     (send b1 :locate #f(0 0 0))
     (send b1 :set-color :blue)
     (setq rleg2 (instance bodyset-link :init (make-cascoords :pos #f(-40 0 5)) :bodies (list b1) :name 'rleg2))
     (send rleg2 :locate #f(120 0 0))
     (send rleg1 :assoc rleg2)

     ;;左もも
     (setq b1 (make-cube 80 10 10))
     (send b1 :locate #f(0 0 0))
     (send b1 :set-color :green)
     (setq lleg1 (instance bodyset-link :init (make-cascoords :pos #f(40 0 5)) :bodies (list b1) :name 'lleg1))
     (send lleg1 :locate #f(-40 0 0))
     (send torso :assoc lleg1)

     ;;左すね
     (setq b1 (make-cube 80 10 10))
     (send b1 :locate #f(0 0 0))
     (send b1 :set-color :blue)
     (setq lleg2 (instance bodyset-link :init (make-cascoords :pos #f(40 0 5)) :bodies (list b1) :name 'lleg2))
     (send lleg2 :locate #f(-120 0 0))
     (send lleg1 :assoc lleg2)

     ;;関節の設定

     (setq joint-list
           (list (instance rotational-joint
                           :init :name 'r-shoulder :parent-link torso :child-link rarm1
                           :axis :y)
                 (instance rotational-joint
                           :init :name 'r-elbow :parent-link rarm1 :child-link rarm2
                           :axis :y)
                 (instance rotational-joint
                           :init :name 'l-shoulder :parent-link torso :child-link larm1
                           :axis :y)
                 (instance rotational-joint
                           :init :name 'l-elbow :parent-link larm1 :child-link larm2
                           :axis :y)
                 (instance rotational-joint
                           :init :name 'r-hip-joint :parent-link torso :child-link rleg1
                           :axis :y)
                 (instance rotational-joint
                           :init :name 'r-knee :parent-link rleg1 :child-link rleg2
                           :axis :y)
                 (instance rotational-joint
                           :init :name 'l-hip-joint :parent-link torso :child-link lleg1
                           :axis :y)
                 (instance rotational-joint
                           :init :name 'l-knee :parent-link lleg1 :child-link lleg2
                           :axis :y)))

     (setq links (list torso rarm1 rarm2 larm1 larm2 rleg1 rleg2 lleg1 lleg2))
     (send self :init-ending)
     self))

  (:r-shoulder (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector num (elt angle-now 1) (elt angle-now 2) (elt angle-now 3) (elt angle-now 4) (elt angle-now 5) (elt angle-now 6) (elt angle-now 7)))
    (send self :angle-vector angle-now))
  (:r-elbow (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector (elt angle-now 0) num (elt angle-now 2) (elt angle-now 3) (elt angle-now 4) (elt angle-now 5) (elt angle-now 6) (elt angle-now 7)))
    (send self :angle-vector angle-now))
  (:l-shoulder (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector (elt angle-now 0) (elt angle-now 1) num (elt angle-now 3) (elt angle-now 4) (elt angle-now 5) (elt angle-now 6) (elt angle-now 7)))
    (send self :angle-vector angle-now))
  (:l-elbow (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector (elt angle-now 0) (elt angle-now 1) (elt angle-now 2) num (elt angle-now 4) (elt angle-now 5) (elt angle-now 6) (elt angle-now 7)))
    (send self :angle-vector angle-now))
  (:r-hip (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector (elt angle-now 0) (elt angle-now 1) (elt angle-now 2) (elt angle-now 3) num (elt angle-now 5) (elt angle-now 6) (elt angle-now 7)))
    (send self :angle-vector angle-now))
  (:r-knee (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector (elt angle-now 0) (elt angle-now 1) (elt angle-now 2) (elt angle-now 3) (elt angle-now 4) num (elt angle-now 6) (elt angle-now 7)))
    (send self :angle-vector angle-now))
  (:l-hip (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector (elt angle-now 0) (elt angle-now 1) (elt angle-now 2) (elt angle-now 3) (elt angle-now 4) (elt angle-now 5) num (elt angle-now 7)))
    (send self :angle-vector angle-now))
  (:l-knee (num)
    (setq angle-now (send self :angle-vector))
    (setq angle-now (float-vector (elt angle-now 0) (elt angle-now 1) (elt angle-now 2) (elt angle-now 3) (elt angle-now 4) (elt angle-now 5) (elt angle-now 6) num))
    (send self :angle-vector angle-now))
  )

(defun 2d-init nil
  (setq *2d-model* (instance 2d-pose-model :init))
  (objects (list *2d-model*))
  (send *2d-model* :angle-vector #f(20 30 -20 -30 40 30 -40 -30)))
