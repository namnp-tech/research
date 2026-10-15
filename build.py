import os, shutil, html

OUT = "/home/claude/MarketingStrategyHub"
shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + "/buoi-hoc"); os.makedirs(OUT + "/tai-nguyen")

COURSE = "Chiến Lược Marketing cho Nhà Quản Trị"
SITE = "Marketing Strategy Hub"
INSTR = "Giảng viên"  # TODO: thay tên giảng viên

# phase -> (label, tailwind color key, hex)
PH = {
    "nen-tang": ("Nền tảng", "Amber", "#D97706"),
    "phan-tich": ("Phân tích", "Sky", "#0284C7"),
    "chien-luoc": ("Hoạch định chiến lược", "Rose", "#E11D48"),
    "trien-khai": ("Triển khai & Đo lường", "Teal", "#0D9488"),
}

S = [
 ("nen-tang","fa-compass","Tổng quan chiến lược marketing & vai trò nhà quản trị",
  "Từ marketing chiến thuật đến tư duy chiến lược gắn với mục tiêu kinh doanh.",
  ["Phân biệt marketing chiến lược và marketing tác nghiệp","Xác định vai trò của CMO/nhà quản trị trong hoạch định chiến lược","Nắm quy trình hoạch định chiến lược marketing 5 bước"],
  ["Marketing chiến lược vs. chiến thuật","Liên kết chiến lược corporate – business – marketing","Quy trình: phân tích → mục tiêu → chiến lược → triển khai → kiểm soát"],
  ["Ansoff Matrix","BCG / GE-McKinsey","Marketing Strategy Canvas"],
  "Thảo luận: một doanh nghiệp bạn biết đang theo đuổi chiến lược marketing nào?",
  "Chọn doanh nghiệp/đơn vị cho đồ án xuyên suốt 9 buổi và mô tả bối cảnh trong 1 trang."),
 ("phan-tich","fa-earth-asia","Phân tích môi trường & lợi thế cạnh tranh",
  "Đọc môi trường vĩ mô, ngành và nội bộ để tìm cơ hội chiến lược.",
  ["Vận dụng PESTEL và 5 Forces vào phân tích ngành","Đánh giá nguồn lực, năng lực cốt lõi của doanh nghiệp","Tổng hợp thành ma trận SWOT/TOWS có hành động"],
  ["Môi trường vĩ mô và xu hướng ngành","Cạnh tranh và định vị đối thủ","Năng lực cốt lõi và lợi thế bền vững (VRIO)"],
  ["PESTEL","Porter's 5 Forces","VRIO","SWOT/TOWS"],
  "Workshop nhóm: lập ma trận TOWS cho doanh nghiệp của đồ án.",
  "Nộp báo cáo phân tích môi trường (tối đa 3 trang)."),
 ("phan-tich","fa-magnifying-glass-chart","Nghiên cứu thị trường & insight khách hàng",
  "Biến dữ liệu thành insight để ra quyết định marketing.",
  ["Thiết kế kế hoạch nghiên cứu thị trường cho quyết định chiến lược","Phân tích hành vi và hành trình khách hàng","Rút ra customer insight có thể hành động"],
  ["Dữ liệu sơ cấp, thứ cấp và dữ liệu số","Customer journey và jobs-to-be-done","Từ dữ liệu đến insight"],
  ["Customer Journey Map","Jobs-to-be-Done","Persona"],
  "Thực hành: xây customer journey map cho một nhóm khách hàng mục tiêu.",
  "Thu thập tối thiểu 5 nguồn dữ liệu về khách hàng của doanh nghiệp đồ án."),
 ("chien-luoc","fa-bullseye","Phân khúc, lựa chọn thị trường mục tiêu & định vị (STP)",
  "Chọn đúng khách hàng và khác biệt hóa trong tâm trí họ.",
  ["Phân khúc thị trường theo nhiều tiêu chí","Đánh giá và lựa chọn thị trường mục tiêu","Xây dựng tuyên bố định vị rõ ràng"],
  ["Tiêu chí phân khúc hiệu quả","Sức hấp dẫn phân khúc và khả năng cạnh tranh","Bản đồ nhận thức và positioning statement"],
  ["Segmentation matrix","Perceptual Map","Positioning Statement"],
  "Nhóm trình bày 3 phương án định vị và phản biện chéo.",
  "Hoàn thiện STP cho doanh nghiệp đồ án."),
 ("chien-luoc","fa-gem","Chiến lược thương hiệu & đề xuất giá trị",
  "Xây dựng tài sản thương hiệu và value proposition khác biệt.",
  ["Hiểu cấu trúc brand equity","Thiết kế value proposition cho từng phân khúc","Lựa chọn chiến lược kiến trúc thương hiệu"],
  ["Brand equity và brand identity","Value Proposition Canvas","Kiến trúc thương hiệu và mở rộng thương hiệu"],
  ["Keller's CBBE","Value Proposition Canvas","Brand Prism"],
  "Case study: một thương hiệu tái định vị thành công.",
  "Viết value proposition và brand promise cho doanh nghiệp đồ án."),
 ("chien-luoc","fa-layer-group","Chiến lược sản phẩm, giá & kênh phân phối",
  "Kết hợp 7Ps thành một hệ thống nhất quán, tạo giá trị và thu về giá trị.",
  ["Quản trị danh mục sản phẩm và vòng đời","Chọn chiến lược định giá phù hợp giá trị cảm nhận","Thiết kế kênh phân phối omni-channel"],
  ["Danh mục sản phẩm và vòng đời","Định giá theo giá trị, cạnh tranh và chi phí","Kênh phân phối và xung đột kênh"],
  ["Product Portfolio","Value-based Pricing","Channel Design"],
  "Bài tập: mô phỏng quyết định giá cho 2 kịch bản thị trường.",
  "Đề xuất bộ 7Ps cho phân khúc mục tiêu."),
 ("trien-khai","fa-bullhorn","Truyền thông tích hợp & marketing số",
  "Phối hợp kênh truyền thông truyền thống và số xoay quanh một thông điệp.",
  ["Xây dựng chiến lược IMC nhất quán","Lựa chọn kênh và định dạng theo hành trình khách hàng","Hiểu vai trò dữ liệu, nội dung và công nghệ"],
  ["IMC và thông điệp cốt lõi","Paid – Owned – Earned media","Marketing số, nội dung và dữ liệu"],
  ["IMC Planner","PESO Model","Funnel AARRR"],
  "Workshop: lập kế hoạch truyền thông 90 ngày.",
  "Nộp kế hoạch IMC 90 ngày."),
 ("trien-khai","fa-chart-line","Đo lường hiệu quả, ngân sách & ROI marketing",
  "Chứng minh giá trị marketing bằng chỉ số mà ban lãnh đạo quan tâm.",
  ["Chọn KPI gắn với mục tiêu chiến lược","Tính ROMI, CAC, CLV","Phân bổ ngân sách marketing hợp lý"],
  ["Marketing metrics và dashboard","CAC, CLV, ROMI","Phương pháp lập và phân bổ ngân sách"],
  ["Balanced Scorecard","CLV/CAC","Budget Allocation"],
  "Thực hành: tính CLV và ROMI trên bộ số liệu mẫu.",
  "Lập ngân sách và hệ thống KPI cho đồ án."),
 ("trien-khai","fa-flag-checkered","Triển khai, tổ chức & trình bày kế hoạch chiến lược",
  "Hợp nhất mọi thành phần thành kế hoạch có thể trình lên hội đồng quản trị.",
  ["Tích hợp kế hoạch marketing chiến lược hoàn chỉnh","Quản trị thay đổi và triển khai nội bộ","Thuyết trình thuyết phục như một nhà quản trị"],
  ["Cấu trúc kế hoạch marketing chiến lược","Tổ chức, nguồn lực, lộ trình và quản trị rủi ro","Kỹ năng pitch trước lãnh đạo"],
  ["Strategic Marketing Plan","Roadmap & OKR","Risk Matrix"],
  "Nhóm thuyết trình đồ án cuối kỳ và nhận phản biện.",
  "Nộp kế hoạch marketing chiến lược hoàn chỉnh."),
]

HEAD = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | {site}</title>
<meta name="description" content="{desc}">
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
body{{background:#EFEFEF;color:#1E293B;font-family:'Plus Jakarta Sans',sans-serif}}
.pin-card{{background:#fff;border-radius:.85rem;box-shadow:0 2px 8px rgba(0,0,0,.06);transition:all .25s}}
.pin-card:hover{{transform:translateY(-4px);box-shadow:0 10px 20px rgba(0,0,0,.12)}}
</style>
</head>
<body class="min-h-screen flex flex-col justify-between antialiased">
"""
FOOT = """<footer class="border-t border-slate-200 bg-white py-6 text-center text-xs text-slate-500">© 2026 {site} • {course}</footer>
</body></html>"""

def head(t, d): return HEAD.format(title=html.escape(t), desc=html.escape(d), site=SITE)
def foot(): return FOOT.format(site=SITE, course=COURSE)

# ---------- index ----------
tags = "".join(
  f'<span onclick="filterTag(\'{k}\')" class="px-3 py-1.5 rounded-md text-white cursor-pointer hover:opacity-90" style="background:{c}">{l}</span>'
  for k,(l,_,c) in PH.items())
cards = ""
for i,(ph,ic,t,sub,obj,cont,tools,act,hw) in enumerate(S,1):
    l,_,c = PH[ph]
    kw = html.escape((t+" "+" ".join(tools)+" "+l).lower())
    cards += f"""<div class="pin-card post-item overflow-hidden flex flex-col justify-between" data-tag="{ph}" data-keywords="{kw}">
<div><div class="p-6 text-white text-center space-y-2" style="background:{c}"><i class="fa-solid {ic} text-4xl"></i><h3 class="font-black text-lg uppercase tracking-wider">Buổi {i}</h3></div>
<div class="p-4 space-y-2"><span class="text-[10px] font-bold uppercase tracking-widest" style="color:{c}">{l}</span>
<h4 class="font-extrabold text-sm text-slate-800 leading-snug">{html.escape(t)}</h4>
<p class="text-xs text-slate-500 leading-relaxed line-clamp-3">{html.escape(sub)}</p></div></div>
<div class="p-4 pt-0"><a href="buoi-hoc/buoi-{i}.html" class="block w-full py-2 bg-slate-100 text-center rounded-lg text-xs font-bold text-slate-700 hover:text-white transition" onmouseover="this.style.background='{c}'" onmouseout="this.style.background=''">Xem chi tiết</a></div></div>
"""
idx = head(COURSE, f"Website học tập 9 buổi môn {COURSE}: nội dung, khung phân tích, bài tập và tài nguyên.") + f"""
<header class="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm">
<div class="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between gap-4">
<a href="index.html" class="flex items-center gap-2.5 shrink-0"><div class="w-9 h-9 rounded-xl bg-rose-600 flex items-center justify-center text-white"><i class="fa-solid fa-chess-knight"></i></div>
<span class="font-black text-xl tracking-tight">Marketing<span class="text-rose-600">Strategy</span></span></a>
<div class="flex-1 max-w-xl mx-4 relative"><input id="searchInput" onkeyup="filterPosts()" placeholder="Tìm kiếm STP, SWOT, brand, ROMI..." class="w-full bg-slate-100 text-xs font-medium pl-10 pr-4 py-2.5 rounded-full border border-slate-200 outline-none focus:bg-white focus:border-rose-600">
<i class="fa-solid fa-magnifying-glass absolute left-3.5 top-3 text-slate-400 text-xs"></i></div>
<a href="about.html" class="bg-slate-100 hover:bg-slate-200 px-3 py-1.5 rounded-full text-xs font-bold text-slate-700 shrink-0">Về môn học</a></div>
<div class="bg-slate-900 px-4 py-2 overflow-x-auto whitespace-nowrap"><div class="max-w-7xl mx-auto flex items-center gap-2 text-xs font-bold text-white">
<span onclick="filterTag('all')" class="px-3 py-1.5 rounded-md bg-slate-600 cursor-pointer">Tất cả 9 buổi</span>{tags}
<a href="https://dapxe.info/tailieu" target="_blank" rel="noopener" class="px-3 py-1.5 rounded-md bg-violet-600"><i class="fa-solid fa-folder-open"></i> Tài nguyên</a></div></div>
</header>
<main class="max-w-7xl mx-auto px-4 py-6 flex-grow w-full space-y-6">
<section class="bg-white rounded-2xl border border-slate-200 p-6"><h1 class="text-2xl font-black">{COURSE}</h1>
<p class="text-sm text-slate-500 mt-1">Lộ trình 9 buổi: từ phân tích môi trường, STP, thương hiệu, 7Ps, truyền thông đến đo lường và trình bày kế hoạch chiến lược.</p></section>
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5" id="postsContainer">{cards}</div></main>
{foot().replace('</body></html>','')}
<script>
function filterPosts(){{const q=document.getElementById('searchInput').value.toLowerCase().trim();
document.querySelectorAll('.post-item').forEach(c=>{{c.style.display=(c.innerText.toLowerCase().includes(q)||c.dataset.keywords.includes(q))?'flex':'none'}})}}
function filterTag(t){{document.querySelectorAll('.post-item').forEach(c=>{{c.style.display=(t==='all'||c.dataset.tag===t)?'flex':'none'}})}}
</script></body></html>"""
open(OUT+"/index.html","w",encoding="utf-8").write(idx)

# ---------- session pages ----------
def ul(items, c): return "".join(f'<li class="flex gap-2"><i class="fa-solid fa-circle-check mt-1 text-xs" style="color:{c}"></i><span>{html.escape(x)}</span></li>' for x in items)
for i,(ph,ic,t,sub,obj,cont,tools,act,hw) in enumerate(S,1):
    l,_,c = PH[ph]
    prev = f'<a href="buoi-{i-1}.html" class="text-xs font-bold text-slate-700 hover:underline"><i class="fa-solid fa-arrow-left"></i> Buổi {i-1}</a>' if i>1 else '<span></span>'
    nxt = f'<a href="buoi-{i+1}.html" class="text-xs font-bold text-slate-700 hover:underline">Buổi {i+1} <i class="fa-solid fa-arrow-right"></i></a>' if i<9 else '<span></span>'
    toolchips = "".join(f'<span class="px-3 py-1 rounded-full text-xs font-bold text-white" style="background:{c}">{html.escape(x)}</span>' for x in tools)
    page = head(f"Buổi {i}: {t}", sub) + f"""
<header class="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm"><div class="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between">
<a href="../index.html" class="font-extrabold flex items-center gap-2 text-sm"><i class="fa-solid fa-arrow-left" style="color:{c}"></i> Quay về Trang Chủ</a>
<span class="text-xs font-bold px-3 py-1 rounded-full border" style="color:{c};border-color:{c}">{l}</span></div></header>
<main class="max-w-4xl mx-auto px-4 py-8 flex-grow w-full space-y-6">
<article class="bg-white p-6 sm:p-10 rounded-2xl border border-slate-200 shadow-sm space-y-6">
<div class="border-b border-slate-100 pb-6 space-y-3"><span class="px-3 py-1 rounded-full text-xs font-extrabold text-white" style="background:{c}">Buổi {i}/9</span>
<h1 class="text-2xl sm:text-3xl font-black leading-tight">{html.escape(t)}</h1><p class="text-sm text-slate-500">{html.escape(sub)}</p></div>
<section><h2 class="text-lg font-extrabold mb-2" style="color:{c}">1. Mục tiêu học tập</h2><ul class="text-sm text-slate-600 space-y-1.5">{ul(obj,c)}</ul></section>
<section><h2 class="text-lg font-extrabold mb-2" style="color:{c}">2. Nội dung chính</h2><ul class="text-sm text-slate-600 space-y-1.5">{ul(cont,c)}</ul></section>
<section><h2 class="text-lg font-extrabold mb-2" style="color:{c}">3. Khung và công cụ</h2><div class="flex flex-wrap gap-2">{toolchips}</div></section>
<section class="p-4 rounded-xl bg-slate-50 border border-slate-200"><h3 class="font-extrabold text-sm"><i class="fa-solid fa-people-group" style="color:{c}"></i> Hoạt động trên lớp</h3><p class="text-sm text-slate-600 mt-1">{html.escape(act)}</p></section>
<section class="p-4 rounded-xl bg-slate-50 border border-slate-200"><h3 class="font-extrabold text-sm"><i class="fa-solid fa-pen-to-square" style="color:{c}"></i> Bài tập sau buổi học</h3><p class="text-sm text-slate-600 mt-1">{html.escape(hw)}</p></section>
<div class="flex justify-between pt-4 border-t border-slate-100">{prev}{nxt}</div></article></main>{foot()}"""
    open(f"{OUT}/buoi-hoc/buoi-{i}.html","w",encoding="utf-8").write(page)

# ---------- about ----------
about = head("Về môn học", f"Thông tin môn {COURSE}") + f"""
<header class="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm"><div class="max-w-4xl mx-auto px-4 h-16 flex items-center">
<a href="index.html" class="font-extrabold flex items-center gap-2 text-sm"><i class="fa-solid fa-arrow-left text-rose-600"></i> Trang Chủ</a></div></header>
<main class="max-w-3xl mx-auto px-4 py-10 flex-grow w-full"><div class="bg-white p-8 rounded-2xl border border-slate-200 shadow-sm space-y-4">
<h1 class="text-2xl font-black">{COURSE}</h1>
<p class="text-sm text-slate-600 leading-relaxed">Môn học gồm 9 buổi, trang bị cho nhà quản trị tư duy và công cụ để hoạch định, triển khai và đo lường chiến lược marketing gắn với mục tiêu kinh doanh. Xuyên suốt khóa, học viên xây dựng một kế hoạch marketing chiến lược hoàn chỉnh cho một doanh nghiệp thực tế.</p>
<p class="text-sm"><strong>Giảng viên:</strong> {INSTR}</p>
<p class="text-sm"><strong>Đánh giá (gợi ý, chỉnh theo đề cương):</strong> chuyên cần và thảo luận, bài tập từng buổi, đồ án cuối kỳ.</p></div></main>{foot()}"""
open(OUT+"/about.html","w",encoding="utf-8").write(about)

# ---------- resources ----------
res = [("Strategic Marketing Plan Template","Khung kế hoạch marketing chiến lược cho đồ án"),
       ("Bộ canvas: STP, Value Proposition, Journey Map","Mẫu điền cho các buổi 3–5"),
       ("Bảng tính CLV / CAC / ROMI","Dùng cho buổi 8"),
       ("Case study và tài liệu đọc thêm","Danh mục theo từng buổi")]
rc = "".join(f'<div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between opacity-80"><div><h3 class="font-bold text-sm">{html.escape(a)}</h3><p class="text-xs text-slate-400">{html.escape(b)}</p></div><span class="px-4 py-2 bg-slate-100 text-slate-500 rounded-xl text-xs font-bold shrink-0"><i class="fa-solid fa-clock"></i> Sắp có</span></div>' for a,b in res)
tn = head("Tài nguyên môn học", "Template, canvas và tài liệu đọc thêm") + f"""
<header class="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm"><div class="max-w-5xl mx-auto px-4 h-16 flex items-center">
<a href="../index.html" class="font-extrabold flex items-center gap-2 text-sm"><i class="fa-solid fa-arrow-left text-violet-600"></i> Trang Chủ</a></div></header>
<main class="max-w-5xl mx-auto px-4 py-8 flex-grow w-full space-y-6"><h1 class="text-2xl font-black">TÀI NGUYÊN MÔN HỌC</h1>
<div class="grid grid-cols-1 md:grid-cols-2 gap-4">{rc}</div></main>{foot()}"""
open(OUT+"/tai-nguyen/index.html","w",encoding="utf-8").write(tn)

open(OUT+"/.nojekyll","w").write("")
open(OUT+"/robots.txt","w").write("User-agent: *\nAllow: /\n")
open(OUT+"/README.md","w",encoding="utf-8").write(f"# {SITE}\nWebsite tĩnh cho môn {COURSE} (9 buổi). Đẩy lên GitHub và bật GitHub Pages.\nSửa nội dung trong `build.py` (danh sách S) rồi chạy `python build.py`.\n")
shutil.copy("/home/claude/build.py", OUT+"/build.py")
print(sorted(os.listdir(OUT)), len(os.listdir(OUT+"/buoi-hoc")))
