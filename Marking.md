# NHẬN XÉT VỀ CÁC THƯ VIỆN XỬ LÝ PDF SANG MARKDOWN
## Nhiệm vụ:  
- Chuyển đổi các file trong tập test thành định dạng markdown 
## 1. Marker PDF
### Tốc độ Xử lý
- **Thời gian xử lý**: ~10 phút (600 giây) cho tài liệu j_0057.pdf (4 trang, tiếng Nhật, nhiều hình ảnh phức tạp)
- **Nhận xét**: Chậm nhất trong 4 thư viện, không phù hợp cho xử lý hàng loạt
- Thực hiện nhiều quá trình trong bước parse pdf 
### Xử lý Text
- **Độ chính xác**: Rất cao - nội dung gần tương tự với tài liệu gốc
- **Cấu trúc markdown**: Rất tốt - phân chia rõ ràng theo cấp (#, ##, ###)
- **Nhận diện heading/subtitle**: Xuất sắc - dễ phân biệt cấp độ tiêu đề

### Xử lý Bảng
- **Khả năng phát hiện**: Tốt - tự động nhận diện vị trí bảng
- **Chất lượng parse**: Bảng được cắt ra riêng biệt và nhúng vào markdown
- **Định dạng**: Markdown table format

### Xử lý Hình Ảnh
- **Khả năng phát hiện**: Xuất sắc - tự động cắt các hình ảnh khỏi PDF
- **Kết quả**: Hình ảnh được lưu riêng biệt với đường dẫn tham chiếu
- **Caption**: Được parse và giữ lại trong markdown

### Đặc điểm Bounding Box
- Hỗ trợ bounding box để định vị chính xác các phần tử
- Tự động nhận diện và tách visual elements

### Ưu điểm
- Độ chính xác text cực cao  
- Cấu trúc markdown rõ ràng  
- Xử lý hình ảnh tốt nhất (cắt riêng biệt)  
- Bảng được xử lý chính xác

### Nhược điểm
- Tốc độ xử lý rất chậm (~10 phút)  
- Không phù hợp cho xử lý lượng lớn PDF  
- Tiêu tốn tài nguyên máy tính cao 



## 2. Docling

### Tốc độ Xử lý
- **Thời gian xử lý**: 82 giây cho tài liệu j_0057.pdf
- **Pipeline**: RapidOCR - tối ưu về tốc độ
- **Nhận xét**: Nhanh hơn Marker PDF ~7.3x lần, phù hợp xử lý hàng loạt

### Xử lý Text
- **Độ chính xác**: Trung bình - nội dung bị thiếu so với tài liệu gốc
- **Cấu trúc markdown**: Chưa tuân thủ chuẩn - thiếu tính nhất quán
- **Nhận diện heading/subtitle**: Yếu - chưa phân chia rõ cấp độ tiêu đề

### Xử lý Bảng
- **Khả năng phát hiện**: Tốt - phát hiện vị trí bảng
- **Chất lượng parse**: Bảng được convert thành cú pháp markdown
- **Định dạng**: Markdown table format

### Xử lý Hình Ảnh
- **Khả năng phát hiện**: Tốt - nhận diện vị trí hình ảnh
- **Kết quả**: Hình ảnh được đánh dấu với comment `<!-- image -->` nhưng không cắt riêng
- **Caption**: Được parse và giữ lại

### Đặc điểm HTML
- Chưa có hỗ trợ các thẻ HTML (<p>, <br/>, v.v.)
- Xuất ra dạng markdown thuần

### Ưu điểm
- Tốc độ xử lý nhanh (82 giây)  
- Phù hợp xử lý batch lớn  
- Nhận diện vị trí visual elements tốt  
- Bảng được parse sang markdow- 
### Nhược điểm
- Độ chính xác text trung bình  
- Nội dung bị mất so với gốc  
- Cấu trúc markdown không chuẩn  
- Hình ảnh không được cắt riêng (chỉ đánh dấu)  
- Không hỗ trợ thẻ HTML- 

## 3. PyMuPDF LLM

### Tốc độ Xử lý
- **Thời gian xử lý**: 5.57 giây cho tài liệu j_0057.pdf
- **Nhận xét**: Nhanh nhất trong 4 thư viện, rất phù hợp xử lý hàng loạt

### Xử lý Text
- **Độ chính xác**: Trung bình - nội dung còn bị thiếu
- **Xuống dòng**: Chưa phù hợp, định dạng text có vấn đề
- **Cấu trúc document**: Yếu - không rõ đâu là Heading, đâu là Subtitle
- **Phân chia cấp bậc**: Không hỗ trợ - toàn bộ text có cùng cấp

### Xử lý Bảng
- **Khả năng phát hiện**: Tốt - phát hiện vị trí bảng
- **Chất lượng parse**: Yếu - định dạng bảng chưa được thể hiện đúng cách
- **Định dạng**: Không phù hợp với markdown table

### Xử lý Hình Ảnh
- **Khả năng phát hiện**: Tốt - nhận diện vị trí hình ảnh
- **Kết quả**: Hình ảnh được đánh dấu nhưng không cắt riêng (giống Docling)
- **Caption**: Được parse và giữ lại

### Đặc điểm HTML
- Hỗ trợ các thẻ HTML đơn giản (br, span)
- Có khả năng sử dụng HTML để định dạng

### Ưu điểm
- Tốc độ xử lý cực nhanh (5.57 giây)  
- Nhanh nhất trong 4 thư viện  
- Phù hợp xử lý lượng lớn PDF  
- Hỗ trợ một số thẻ HTML

### Nhược điểm
- Độ chính xác text thấp  
- Nội dung bị thiếu nhiều  
- Cấu trúc markdown không rõ ràng  
- Không phân chia cấp bậc tiêu đề  
- Xử lý bảng kém  
- Hình ảnh không cắt riêng  
- Xuống dòng không phù hợp 


## 4. Mineru

### Tốc độ Xử lý
- **Thời gian xử lý**: Thời gian xử lý ở mức độ trung bình. Nhìn chung chạy ở chế độ Backend thì vẫn nhanh hơn Marker Pdf 
- **Nhận xét**: Tốc độ phù hợp cho việc xử lý ảnh, chỉ chậm hơn Marker pdf một chút nhưng kết quả đem lại vẫn khá tốt, số lượng ảnh nhận biết nhiều. Đặc biệt có cung cấp các file json, hỗ trợ cho mô hình biết được cấu trúc của document. Ngoài ra còn có cái file pdf, đánh dấu bouding box cho các visual element => Rất là phù hợp cho việc xử lý trong model AI 

### Xử lý Text
- **Độ chính xác**: Cần kiểm tra
- **Cấu trúc markdown**: Cấu trúc có phân cách, hợp với document gốc. Ngoài ra còn có các file json hỗ trợ cấu trúc
- **Nhận diện heading/subtitle**: Tốt hơn. 

### Xử lý Bảng
- **Khả năng phát hiện**: Tốt 
- **Định dạng**: Bảng được chuyển thành dạng HTML thay vì định dạng markdown như MarkerPdf. Điều này phù hợp hơn trong trường hợp gặp các mô hình bảng phức tạp, đặc biệt là trong các bài báo cáo về kinh doanh. 

### Xử lý Hình Ảnh
- **Khả năng phát hiện**: Cần kiểm tra
- **Kết quả**: Cần kiểm tra
- **Caption**: Cần kiểm tra

### Đặc điểm
- Chỉ có thể chạy model với tham số backend, có hỗ trợ chạy với lvvm (sẽ hỗ trợ parse document tốt hơn), tuy nhiên cần phải có cấu hình máy đủ mạnh (hoặc do cái máy e yếu.)

### Ưu điểm
- Nhận diện và xử lý cấu trúc tốt 
- Nội dng text được viết rõ ràng, Marker Pdf có vẻ loạn hơn một chút so với Mineru. 

### Nhược điểm
- Chưa thấy nữa, cần nghiên cứu thêm 
--- 

## Xếp Hạng Theo Tiêu Chí

### 1. Tốc độ Xử lý (Nhanh → Chậm)
1. **PyMuPDF LLM**:  
2. **Docling**:  
3. **Mineru** 
4. **Marker PDF**: 

### 2. Chất Lượng Output (Cao → Thấp)
1. **Marker PDF**: Xuất sắc - text chính xác, cấu trúc rõ ràng
2. **Docling**: Tốt - nhanh và cân bằng
3. **PyMuPDF LLM**: Tạm chấp nhận - nhanh nhưng chất lượng thấp
4. **Minery**: Xuát sắc - text chính xác, cấu trúc rõ ràng. Cung cấp đầy đủ các file JSON về cấu trúc và file nhận diện bảng. 
### 3. Xử lý Visual Elements (Bảng/Hình)
1. **Marker PDF**: Cắt riêng 
2. **Docling**: Đánh dấu bảng đúng
3. **PyMuPDF LLM**: Đánh dấu, định dạng kém
4. **Mineru**: Căt riêng, kết quả tốt nhất. 
---

## Khuyến Nghị Sử Dụng

- **Chất lượng tối ưu**: Sử dụng **Marker PDF** (chấp nhận tốc độ chậm)
- **Cân bằng tốc độ/chất lượng**: Sử dụng **Docling**
- **Tốc độ tối ưu**: Sử dụng **PyMuPDF LLM** (chấp nhận chất lượng thấp)
- **Cung cấp dataset tốt cho model**: Mineru