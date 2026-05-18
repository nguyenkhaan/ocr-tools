# BÁO CÁO ĐÁNH GIÁ CÁC THƯ VIỆN CHUYỂN PDF SANG MARKDOWN

## 1. 

## 2. Tiêu chí đánh giá

Mỗi công cụ được đánh giá theo các nhóm tiêu chí sau:

- Giới thiệu công cụ
- Khả năng xử lý text
- Khả năng xử lý visual element
- Tốc độ xử lý
- Ưu điểm và nhược điểm
- Kết luận

## 3. Đánh giá chi tiết từng công cụ

## 3.1. Marker PDF

### Giới thiệu công cụ

`Marker PDF` là công cụ chuyển đổi PDF sang Markdown với chất lượng đầu ra cao, đặc biệt mạnh ở việc giữ lại cấu trúc tài liệu và tách riêng các thành phần như bảng, hình ảnh.

### Khả năng xử lý

#### Xử lý text

- Độ chính xác văn bản rất cao, nội dung đầu ra gần với tài liệu gốc.
- Cấu trúc Markdown rõ ràng, có phân cấp tiêu đề như `#`, `##`, `###`.
- Khả năng nhận diện heading và subtitle tốt, giúp tài liệu dễ đọc và dễ dùng lại.

#### Visual Element

- Nhận diện bảng tốt và có thể đưa bảng vào nội dung đầu ra.
- Hình ảnh được phát hiện và tách riêng khỏi PDF.
- Caption của hình ảnh có thể được giữ lại trong Markdown.
- Có hỗ trợ thông tin định vị như bounding box, thuận lợi nếu cần xử lý sâu hơn.

#### Tốc độ xử lý

- Tốc độ xử lý chậm.
- Theo ghi chú tham khảo, thời gian xử lý khoảng `10 phút` cho file `j_0057.pdf` gồm 4 trang, nhiều hình ảnh và nội dung phức tạp.
- Không phù hợp nếu cần xử lý hàng loạt trong thời gian ngắn.

### Ưu điểm

- Chất lượng text tốt nhất trong nhóm được đánh giá.
- Giữ cấu trúc tài liệu rõ ràng.
- Xử lý hình ảnh và bảng tốt.
- Phù hợp khi ưu tiên chất lượng đầu ra.

### Nhược điểm

- Tốc độ xử lý rất chậm.
- Tiêu tốn tài nguyên tính toán nhiều hơn các công cụ khác.
- Không phải lựa chọn tối ưu cho batch lớn.

### Kết luận

`Marker PDF` phù hợp khi mục tiêu chính là chất lượng chuyển đổi sang Markdown. Đây là lựa chọn tốt cho các tài liệu cần giữ nguyên cấu trúc, nội dung và visual element, nhưng cần chấp nhận đánh đổi về tốc độ.

## 3.2. MinerU

### Giới thiệu công cụ

`MinerU` là công cụ xử lý PDF có định hướng mạnh về phân tích cấu trúc tài liệu. Ngoài Markdown, công cụ này còn cung cấp thêm các file hỗ trợ như JSON hoặc thông tin bố cục, thuận lợi cho các bài toán AI và document understanding.

### Khả năng xử lý

#### Xử lý text

- Nội dung văn bản nhìn chung rõ ràng và dễ đọc.
- Cấu trúc tài liệu được giữ khá tốt, gần với bố cục gốc.
- Khả năng nhận diện heading và subtitle ở mức khá.
- Một số điểm về độ chính xác văn bản vẫn cần kiểm tra thêm để có kết luận chắc chắn hơn.

#### Visual Element

- Khả năng nhận diện bảng tốt.
- Bảng thường được biểu diễn dưới dạng HTML thay vì Markdown table.
- Cách biểu diễn này phù hợp hơn với các bảng phức tạp.
- Có thêm file JSON và dữ liệu cấu trúc, hỗ trợ tốt cho việc phân tích document bằng mô hình AI.
- Theo ghi chú tham khảo, công cụ còn có khả năng sinh file PDF kèm bounding box cho visual element.

#### Tốc độ xử lý

- Tốc độ ở mức trung bình.
- Nhanh hơn `Marker PDF` trong nhiều trường hợp, đặc biệt khi chạy với chế độ backend.
- Phù hợp hơn cho các bài toán cần cân bằng giữa chất lượng cấu trúc và hiệu năng.

### Ưu điểm

- Giữ cấu trúc tài liệu tốt.
- Nội dung text dễ đọc.
- Xử lý bảng tốt, nhất là bảng phức tạp.
- Có thêm dữ liệu JSON và thông tin layout rất hữu ích cho AI pipeline.

### Nhược điểm

- Một số tiêu chí về text và hình ảnh vẫn cần kiểm chứng thêm.
- Việc chạy các chế độ mạnh hơn có thể yêu cầu cấu hình máy cao.
- Chưa phải công cụ dễ đánh giá nhanh nếu chỉ nhìn vào mỗi file Markdown đầu ra.

### Kết luận

`MinerU` là lựa chọn đáng chú ý khi không chỉ cần Markdown mà còn cần dữ liệu cấu trúc phục vụ xử lý tài liệu nâng cao. Công cụ này phù hợp với các bài toán nghiên cứu, AI, hoặc trích xuất document có nhiều thành phần phức tạp.

## 3.3. PyMuPDF4LLM

### Giới thiệu công cụ

`PyMuPDF4LLM` là thư viện tối ưu cho việc trích xuất nội dung PDF nhanh để phục vụ các hệ thống LLM hoặc pipeline xử lý văn bản tự động.

### Khả năng xử lý

#### Xử lý text

- Tốc độ trích xuất text rất nhanh.
- Tuy nhiên độ chính xác nội dung chỉ ở mức trung bình.
- Một số phần nội dung có thể bị thiếu.
- Cấu trúc Markdown chưa tốt, khó phân biệt đâu là heading, đâu là subtitle.
- Việc xuống dòng và trình bày văn bản còn chưa tự nhiên.

#### Visual Element

- Có thể phát hiện vị trí bảng và hình ảnh.
- Hình ảnh thường chỉ được đánh dấu thay vì tách riêng hoàn chỉnh.
- Caption có thể được giữ lại.
- Bảng được nhận diện nhưng cách biểu diễn chưa tốt, có cung cấp cách biểu diễn markdown cho các bảng đơn giản, cũng như HTML luôn. 
- Có hỗ trợ một số thẻ HTML đơn giản để hỗ trợ định dạng.

#### Tốc độ xử lý

- Là công cụ nhanh nhất trong 4 thư viện được đánh giá.
- Theo ghi chú tham khảo, thời gian xử lý khoảng `5.57 giây` cho file `j_0057.pdf`.
- Phù hợp khi ưu tiên tốc độ hoặc cần xử lý số lượng lớn tài liệu.

### Ưu điểm

- Tốc độ xử lý rất nhanh.
- Dễ phù hợp với các hệ thống cần throughput cao.
- Có thể dùng tốt trong các pipeline xử lý sơ bộ.

### Nhược điểm

- Chất lượng Markdown chưa cao.
- Nội dung text có thể thiếu.
- Cấu trúc tài liệu chưa rõ ràng.
- Xử lý bảng và hình ảnh chưa thật sự tốt nếu so với yêu cầu báo cáo hoàn chỉnh.

### Kết luận

`PyMuPDF4LLM` phù hợp khi ưu tiên tốc độ hơn chất lượng trình bày. Nếu mục tiêu là lấy nội dung nhanh để đưa vào pipeline xử lý tiếp theo thì đây là lựa chọn tốt. Nếu cần Markdown đẹp và gần với tài liệu gốc thì công cụ này chưa phải phương án tối ưu.

## 3.4. Docling

### Giới thiệu công cụ

`Docling` là công cụ xử lý tài liệu hướng tới khả năng chuyển đổi nhanh và hỗ trợ nhận diện nhiều thành phần trong PDF. Đây là lựa chọn khá cân bằng giữa tốc độ và khả năng phân tích tài liệu.

### Khả năng xử lý

#### Xử lý text

- Độ chính xác văn bản ở mức trung bình.
- Một số nội dung có thể bị thiếu so với bản gốc.
- Cấu trúc Markdown chưa thật sự nhất quán.
- Khả năng phân biệt heading và subtitle chưa mạnh.

#### Visual Element

- Có thể nhận diện bảng và chuyển sang cú pháp Markdown.
- Có thể phát hiện hình ảnh trong tài liệu.
- Hình ảnh thường được đánh dấu bằng comment như `<!-- image -->` thay vì tách riêng.
- Caption của hình ảnh vẫn có thể được giữ lại.

#### Tốc độ xử lý

- Tốc độ khá nhanh.
- Theo ghi chú tham khảo, thời gian xử lý khoảng `82 giây` cho file `j_0057.pdf`.
- Nhanh hơn `Marker PDF` khá nhiều, phù hợp hơn cho xử lý số lượng lớn.

### Ưu điểm

- Tốc độ xử lý tốt.
- Có khả năng nhận diện các visual element tương đối ổn.
- Phù hợp với nhu cầu xử lý batch hơn `Marker PDF`.

### Nhược điểm

- Chất lượng text chưa cao bằng `Marker PDF`.
- Cấu trúc Markdown chưa thật sự đẹp và chuẩn.
- Hình ảnh chưa được cắt riêng thành file rõ ràng.

### Kết luận

`Docling` là lựa chọn cân bằng giữa tốc độ và khả năng xử lý tài liệu. Công cụ này phù hợp khi cần hiệu năng tốt hơn nhưng vẫn muốn giữ được một phần cấu trúc và visual element trong đầu ra Markdown.

## 4. So sánh tổng quan

| Công cụ | Text | Visual Element | Tốc độ | Nhận xét nhanh |
|---|---|---|---|---|
| `Marker PDF` | Rất tốt | Rất tốt | Chậm | Chất lượng đầu ra cao nhất |
| `MinerU` | Khá tốt | Tốt | Trung bình | Mạnh về cấu trúc và dữ liệu hỗ trợ |
| `PyMuPDF4LLM` | Trung bình | Trung bình | Rất nhanh | Phù hợp khi ưu tiên tốc độ |
| `Docling` | Trung bình | Khá | Nhanh | Lựa chọn cân bằng |

## 5. Kết luận chung

Mỗi công cụ có một điểm mạnh riêng, vì vậy việc lựa chọn phụ thuộc vào mục tiêu sử dụng:

- Nếu ưu tiên **chất lượng Markdown** và độ sát với tài liệu gốc: chọn `Marker PDF`.
- Nếu ưu tiên **dữ liệu cấu trúc và khả năng hỗ trợ AI pipeline**: chọn `MinerU`.
- Nếu ưu tiên **tốc độ xử lý nhanh nhất**: chọn `PyMuPDF4LLM`.
- Nếu cần **cân bằng giữa tốc độ và chất lượng**: chọn `Docling`.

Nhìn chung, không có công cụ nào tốt nhất trong mọi trường hợp. Với bài toán chuyển PDF sang Markdown, nên chọn công cụ dựa trên yêu cầu thực tế về chất lượng đầu ra, visual element và thời gian xử lý.
