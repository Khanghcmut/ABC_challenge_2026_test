**Overview:**

* Gồm 2 loại file với (1\_sbj\_\*) là training data còn (2\_sbj\_\*) là test data  
* Gía trị ngoại lai (outliers) xuất hiện nhiều

**Trục x-axis, y-axis và z-axis được xác định qua 1 đoạn trong bài báo:**   
 “Secondly, the raw accelerometer data reveals limb orientation through its alignment with the Earth’s gravitational field, a constant downward force of 1g. This static component acts as a stable reference vector. For example, when a participant is lying down to perform a sit-up, the y-axis of an accelerometer placed on the ankle would align with the downward gravitational vector. In contrast, during standing-based activities, the x-axis of a sensor on the hand might align with gravitational orientation, thus providing crucial contextual information about the participant’s posture.”  
\=\> Xét 1 người khi đứng thẳng và áp sát lòng bàn tay (bàn tay xòe ra) vào thân người thì trục x sẽ cùng chiều với chiều 4 ngón tay, trục y là trục ngược chiều với ngón tay cái và trục z sẽ là vuông góc với mu / lòng bàn tay.

**Vấn đề:**  
Em nghĩ nằm ở chuyện tay người đeo đồng hồ đã xoay 1 góc 180 độ và úp mặt đồng hồ vào trong da tay thay vì nằm hướng ra ngoài (Nếu trục x y z của em lấy từ dữ kiện vấn đề 1 )

**Chứng minh:**

* Tại đồ thị theo trục x, ta có thể thấy được là trung vị ở các  “arm\_acc\_x” ngược dấu với “leg\_acc\_x” mà trục x là trục trùng với vecto trọng lực nên khi trung vị của “arm\_acc\_x” ngược dấu có nghĩa rằng người đeo đã xoay đồng hồ 1 góc 180 độ  
* Còn đồ thị trục z, ta có thể thấy rằng trung vị của “arm\_acc\_z” hầu như ngược dấu so với “leg\_acc\_z” mà trục z là trục vuông góc với mu/lòng bàn tay thì có nghĩa là người đeo đã úp mặt đồng hồ vào trong

