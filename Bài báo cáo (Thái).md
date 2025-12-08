**Note:**

* Người 1: “1\_sbj\_0”  
* Người 2: “1\_sbj\_0\_2”  
* Người 3: “1\_sbj\_1”  
* Người 4: “1\_sbj\_2”  
* Người 5: “2\_sbj\_0”  
* Người 6: “2\_sbj\_0\_2”  
* Người 7: “2\_sbj\_1”  
* Người 8: “2\_sbj\_2”

**Những gì em Chú ý được:**   
	1/ Các cột trong file train (1\_\*) và file test (2\_\*) bị đảo ngược  
	2/ Giá trị max, min và std nó cách biệt quá lớn (Điều này có thể do thể chất của mỗi người hoặc do vị trí cảm biến)

**Vấn đề 1: Bài báo kêu rằng**   
“Secondly, the raw accelerometer data reveals limb orientation through its alignment with the Earth’s gravitational field, a constant downward force of 1g. This static component acts as a stable reference vector. For example, when a participant is lying down to perform a sit-up, the y-axis of an accelerometer placed on the ankle would align with the downward gravitational vector. In contrast, during standing-based activities, the x-axis of a sensor on the hand might align with gravitational orientation, thus providing crucial contextual information about the participant’s posture.”

* Theo bản thân em dịch được là khi nằm để thực hiện động tác “sits up” thì trục y ở mắt cá chân sẽ cùng chiều với vecto trọng lực, còn khi thực hiện động tác đứng thì trục x sẽ cùng chiều với vecto trọng lực  
* Theo cách tư duy của em, khi xét 1 người đang đứng thẳng ( cánh tay áp sát vào người và tay xòe ra ) thì trục X sẽ trục có chiều theo 4 ngón tay, trục Y sẽ là trục có chiều ngược lại với ngón cái còn trục Z sẽ là trục vuông góc với mu/lòng bàn tay

**\+ )Nhưng có 1 vấn đề khi em xét thử ví dụ của người 1 (file 1\_sbj\_0) khi làm động tác sits-up:**

* Xét 4s hành động sits-up của người đó thì em thấy giá trị “leg\_acc\_x” và “leg\_acc\_y” lại đối nhau (1g và \-1g). Điều đó có nghĩa là 2 trục này đối nhau nên em thấy hơi lạ. Trong khi trục y là trục cùng chiều với vecto trọng lực hướng xuống thì đáng lẽ nó phải mang giá trị dương.

**\+)Khi xét 1 hành động đứng như “stretching (triceps) thì hướng tư duy của em lại trùng khớp**  
**Vấn đề 2: em nghĩ nằm ở chuyện tay người đeo đồng hồ đã xoay 1 góc 180 độ và úp mặt đồng hồ vào trong da tay thay vì nằm hướng ra ngoài (Nếu trục x y z của em lấy từ dữ kiện vấn đề 1 )**

**Chứng minh:**

* Tại đồ thị theo trục x, ta có thể thấy được là trung vị ở các  “arm\_acc\_x” ngược dấu với “leg\_acc\_x” mà trục x là trục trùng với vecto trọng lực nên khi trung vị của “arm\_acc\_x” ngược dấu có nghĩa rằng người đeo đã xoay đồng hồ 1 góc 180 độ  
* Còn đồ thị trục z, ta có thể thấy rằng trung vị của “arm\_acc\_z” hầu như ngược dấu so với “leg\_acc\_z” mà trục z là trục vuông góc với mu/lòng bàn tay thì có nghĩa là người đeo đã úp mặt đồng hồ vào trong

**\=\> Những người úp mặt đồng hồ vào trong da tay:**

* Người 1 (xoay 180 độ)  
* Người 2 (xoay 180 độ)  
* Người 3 (xoay 180 độ)  
* Người 4  
* Người 5  
* Người 6  
* Người 7  
* Người 8 (xoay 180 độ)


**\*Note:** special thankss to bài báo của anh gửi chứ để em có hướng đi chứ ko là em mù tịt về cái dataset này luôn. Em không rõ là cách làm của em có hợp lý không nhưng mà ít ra em vẫn có hướng kekekeke