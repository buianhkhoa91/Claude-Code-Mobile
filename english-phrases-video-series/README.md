# 300 Bài Cụm Từ Tiếng Anh Thông Dụng Cho Người Đi Làm

Chuỗi 300 video short (~60 giây/video) dạy cụm từ tiếng Anh thông dụng (Phrasal Verbs, Idioms, Collocations, Fixed Expressions) cho người Việt đi làm trong nhiều lĩnh vực: văn phòng, IT, HR, tài chính, sales/marketing, logistics, sản xuất, nhà hàng – khách sạn, y tế, quản lý, khởi nghiệp...

## Cấu trúc mỗi bài (video ~60 giây, 12 Scene)

- **Scene 1 – Hook**: giới thiệu chủ đề bài học (voice tiếng Việt).
- **Scene 2–11 – Nội dung**: 5 cụm từ, mỗi cụm từ chiếm 2 scene:
  - *Scene cụm từ*: đọc cụm từ tiếng Anh (giọng Anh-Mỹ); hiển thị cụm từ + IPA chuẩn Oxford (NAmE) + nghĩa tiếng Việt (không đọc).
  - *Scene ví dụ*: đọc câu ví dụ tiếng Anh (giọng Anh-Mỹ); hiển thị câu ví dụ + bản dịch tiếng Việt (không đọc).
- **Scene 12 – CTA**: "Nghe và lặp lại để ghi nhớ" + giới thiệu bài tiếp theo "Bài {N+1} – {Chủ đề}".

> Ghi chú: yêu cầu gốc nêu "mỗi bài 5 cụm từ" và "10 scene nội dung" — hai con số này được dung hòa bằng cách mỗi cụm từ chiếm 2 scene (cụm từ + ví dụ) = 10 scene nội dung.

## Cấu trúc thư mục

- `00-Muc-Luc-300-Bai.docx` — mục lục 30 chương × 10 bài, kèm danh sách 5 cụm từ của từng bài.
- `scripts-docx/` — 300 file kịch bản, mỗi video 1 file: `Bai-NNN-<chu-de>.docx`.
- `data/outline.json` — mục lục dạng dữ liệu (30 modules × 10 lessons).
- `data/lessons-*.json` — toàn bộ nội dung 300 bài (1.500 cụm từ) dạng JSON: cụm từ, IPA, nghĩa, ví dụ, dịch ví dụ, hook.
- `tools/render_docx.py` — sinh lại toàn bộ file .docx từ JSON (`python3 tools/render_docx.py`, cần `pip install python-docx`).
- `tools/check_data.py` — kiểm tra dữ liệu: đủ 300 bài, đủ 5 cụm từ/bài, trùng lặp cụm từ giữa các bài.

## Quy trình cập nhật nội dung

1. Sửa nội dung trong `data/lessons-*.json` (hoặc chủ đề trong `data/outline.json`).
2. Chạy `python3 tools/check_data.py` để kiểm tra.
3. Chạy `python3 tools/render_docx.py` để sinh lại các file .docx.
