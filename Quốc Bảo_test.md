Em tên là: Trịnh Quốc Bảo  
Học tại: Trường Đại học Bách Khoa Thành phố Hồ Chí Minh  
Ngành: Khoa học dữ liệu  
Khoá: K25  
Em có tìm ra vấn đề là arm\_acc\_x của participant 2 bị ngược chiều, khi em nhận ra vấn đề và tìm lí do cho vấn đề (đeo ngược tay, ngược đồng hồ), em cũng nhận ra là khi mà mình đeo ngược vậy thì sẽ phải quay 2 trục 1 lúc, nhưng em ko biết đó là do mấy anh gài ạ.   
Pipeline Xử Lý Và Huấn Luyện Mô Hình Dự Đoán Hành Động:

1. Load dữ liệu và gán participant ID  
   * Quét toàn bộ file CSV trong thư mục dữ liệu.  
   * Gán mã participant dựa vào tên file thông qua một bảng mapping.  
   * Gộp dữ liệu train và test thành hai DataFrame chính.  
2. Thực hiện EDA (Exploratory Data Analysis)  
   * Kiểm tra phân bố mẫu theo hành động và participant.  
   * Vẽ boxplot, histogram, KDE cho các trục arm\_acc và leg\_acc.  
   * So sánh giá trị trung bình và độ lệch chuẩn giữa các participant theo từng hành động.  
   * Phát hiện sự bất thường của participant 2 ở trục arm\_acc\_x (dấu bị đảo ngược).  
3. Chuẩn hóa dữ liệu – Điều chỉnh hướng trục arm\_acc\_x của participant 2  
   * Chỉ riêng participant 2 có hướng trục arm\_acc\_x ngược so với các participant khác.  
   * Áp dụng phép đổi dấu (x \= \-x) cho participant 2 trên cả tập train và test.  
   * Lưu lại hai bộ dữ liệu đã chỉnh sửa (df\_train\_later, df\_test\_later) để dùng cho bước trích xuất đặc trưng.  
4. Trích xuất đặc trưng bằng Sliding Window  
   * Cửa sổ kích thước 50, overlap 20\.  
   * Với mỗi biến số, tính mean, std, min, max theo cửa sổ.  
   * Gán nhãn cho từng cửa sổ bằng mode của nhãn trong cửa sổ.  
   * Sinh ra X\_train, y\_train, X\_test, y\_test.  
5. Chuẩn bị dữ liệu cho mô hình  
   * Shuffle dữ liệu để tránh bias theo thời gian.  
   * Chia train/validation theo stratified split để giữ tỷ lệ lớp.  
   * Xác định số lượng lớp thực tế của bài toán.  
6. Huấn luyện mô hình XGBoost  
   * Sử dụng XGBClassifier với các tham số chính:  
     n\_estimators \= 80, max\_depth \= 6, learning\_rate \= 0.1.  
   * Huấn luyện với train và validation set.  
   * Theo dõi logloss trong quá trình huấn luyện.  
7. Đánh giá mô hình  
   * Tính accuracy trên validation và test set.  
   * Xuất classification report.  
   * Vẽ confusion matrix (đủ lớp và loại bỏ label 0 nếu cần).  
8. Xuất kết quả và báo cáo  
   * Tổng hợp accuracy, lỗi nhận dạng, confusion matrix.  
   * Ghi nhận cải thiện sau khi điều chỉnh dấu của participant 2\.

