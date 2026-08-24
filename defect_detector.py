from ultralytics import YOLO


class ConcreteDefectDetector:

    def __init__(self, model_path="models/best.pt"):
        self.model = YOLO(model_path)

    def detect(self, image):

        results = self.model.predict(
            source=image,
            conf=0.25,
            save=False
        )

        result = results[0]

        detections = []

        if result.boxes is not None:

            for box in result.boxes:

                class_id = int(box.cls[0])
                confidence = float(box.conf[0])

                class_name = result.names[class_id]

                coordinates = box.xyxy[0].tolist()

                detections.append({
                    "defect": class_name,
                    "confidence": confidence,
                    "box": coordinates
                })

        return result, detections
