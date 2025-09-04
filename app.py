import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="صفوة لفرز السير الذاتية", layout="wide")

# تضبيطات شكل ستريملت عشان يطلع احترافي أكثر
st.markdown("""
<style>
/* اخفاء هيدر/فوتر وتخفيف الحواف الافتراضية */
#MainMenu, footer, header {visibility: hidden;}
[data-testid="stSidebar"] {background: transparent;}
[data-testid="stAppViewContainer"] > .main {padding-top: 0rem; padding-bottom: 0rem;}
/* توحيد خلفية التطبيق مع واجهتك */
html, body, [data-testid="stAppViewContainer"] {
  background: #fafaf3 !important;
}
</style>
""", unsafe_allow_html=True)

html = r"""
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <title>صفوة لفرز السير الذاتية</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800;900&display=swap');

    :root{
      --bg:#fafaf3; 
      --ink:#182A4E;
      --field:#fff;
      --field-b:#D8DDE1;
      --accent:#3B7C74;
      --accent-ink:#fff;
      --card:#182A4E;
    }

    /* أساسيات */
    *{box-sizing:border-box}
    body{
      margin:0;
      background:var(--bg);
      color:var(--ink);
      font-family:"Cairo", -apple-system, system-ui, "Noto Sans Arabic", sans-serif;
    }

    /* حاوية مركزية أعرض مع نفس الماكس ويدث */
    .container{max-width:1200px;margin:0 auto;padding:0 20px;}

    /* الهيدر */
    .site-header{display:flex;align-items:center;gap:14px;border-bottom:1px solid #E5E7EB;padding:14px 0}
    .brand{display:flex;align-items:center;gap:12px;flex-direction:row-reverse}
    .header-logo{height:72px;width:auto;object-fit:contain} /* طلبك: 72px */
    .brand-title{font-weight:900;font-size:24px}

    /* التخطيط العام */
    .grid{display:grid;gap:28px;grid-template-columns:1fr}
    @media(min-width:1024px){.grid{grid-template-columns:minmax(0,1fr) 360px}}

    /* العناوين والمحتوى */
    .kicker{font-size:28px;font-weight:900;margin:10px 0 12px}

    .meta{display:grid;gap:10px;grid-template-columns:repeat(3,1fr);margin:14px 0}
    .meta-box{
      background:var(--field);
      border:1px solid var(--field-b);
      border-radius:14px;
      padding:12px 14px;
      text-align:center;
      font-weight:700;
      color:#243b53;
    }

    .hint{color:#223b65;font-weight:800;font-size:16px;margin:8px 0}

    .fields{display:flex;flex-direction:column;gap:10px;margin-bottom:16px}
    .chip-input{
      background:#fff;border:1px solid var(--field-b);border-radius:14px;padding:12px 14px;font-size:16px
    }

    .cta-inline{display:flex;flex-direction:column;gap:10px;margin-top:6px}
    .attach{background:#e8f3f1;border:1px dashed var(--accent);padding:12px;border-radius:14px;font-weight:800}
    .upload{background:#fff;border:1px solid var(--field-b);padding:12px;border-radius:14px;cursor:pointer}
    .upload input{display:none}
    .cta{
      padding:14px 20px;border-radius:14px;background:var(--accent);color:var(--accent-ink);
      font-weight:800;border:none;cursor:pointer;box-shadow:0 6px 16px rgba(59,124,116,.35)
    }

    /* السايدبار */
    .side{
      background:var(--card);color:#fff;border-radius:18px;padding:18px;
      box-shadow:0 10px 28px rgba(0,0,0,.14)
    }
    .side h3{margin:0 0 12px}
    .preset{width:100%;padding:10px;border-radius:12px;border:1px solid #2f4680;background:#0f2144;color:#fff}

    .format-toggle{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
    .pill{
      padding:10px;border-radius:12px;border:1px solid #3b4f85;background:#0f2144;color:#e5ecff;
      font-weight:800;cursor:pointer;transition:transform .05s ease
    }
    .pill:active{transform:translateY(1px)}
    .pill.active{background:#25407a}

    .review{margin-top:10px}
    .review-title{font-weight:800;margin-bottom:6px}
    .reset{
      width:100%;padding:10px;border-radius:12px;border:1px solid #3d5aa6;background:#11305e;color:#fff;
      font-weight:800;cursor:pointer;margin-top:10px
    }

    /* مسافات أخف أعلى/أسفل لتقليل الفراغ حول الإطار المضمن */
    .page-pad{padding:8px 0 20px}
  </style>
</head>
<body>
  <div class="page-pad">
    <header class="site-header container">
      <div class="brand">
        <img src="https://i.postimg.cc/T2QkYzWn/safwa-logo.png" alt="شعار صفوة" class="header-logo">
        <div class="brand-title">صفوة لفرز السير الذاتيه</div>
      </div>
    </header>

    <main class="container grid">
      <!-- المحتوى الرئيسي -->
      <section class="content">
        <h1 class="kicker">فرز السير الذاتية بشكل آلي</h1>

        <div class="meta">
          <div class="meta-box">الجامعة</div>
          <div class="meta-box">التخصص</div>
          <div class="meta-box">الجنسية</div>
        </div>

        <div class="hint">الشرط البحثي واحد او اكثر</div>

        <div class="fields">
          <input id="uni" class="chip-input" placeholder="مثال: King Saud University">
          <input id="nation" class="chip-input" placeholder="مثال: سعودية">
          <input id="major" class="chip-input" placeholder="مثال: نظم المعلومات الإدارية، علوم حاسب…">
          <input id="extra" class="chip-input" placeholder="جملة شرطية إضافية…">
        </div>

        <div class="cta-inline">
          <div id="attachLabel" class="attach">إرفاق ملفات CV (PDF)</div>
          <label class="upload">
            <input id="fileInput" type="file" multiple accept=".pdf"/>
            اختر ملفاتك…
          </label>
          <button class="cta" id="startBtn">ابدأ الفرز الآن</button>
        </div>
      </section>

      <!-- السايدبار -->
      <aside class="side">
        <h3>الإعدادات</h3>
        <div class="row">
          <select id="preset" class="preset">
            <option>Preset (KSU + MIS)</option>
            <option>KSU Only</option>
            <option>MIS Only</option>
          </select>
        </div>

        <div class="row">
          <div class="format-toggle" id="formatToggle">
            <button class="pill active" data-fmt="PDF">PDF</button>
            <button class="pill" data-fmt="XLSX">XLSX</button>
            <button class="pill" data-fmt="CSV">CSV</button>
          </div>
        </div>

        <div class="review">
          <div class="review-title">اختياراتك الحالية:</div>
          <ul>
            <li><span>الجامعة:</span> <b id="rUni">—</b></li>
            <li><span>الجنسية:</span> <b id="rNation">—</b></li>
            <li><span>التخصص:</span> <b id="rMajor">—</b></li>
            <li><span>شرط إضافي:</span> <b id="rExtra">—</b></li>
          </ul>
        </div>

        <div class="row">
          <button id="resetBtn" class="reset">Reset</button>
        </div>
      </aside>
    </main>
  </div>

  <script>
    // JS للتبديل والتحديث
    const pills = document.querySelectorAll(".pill");
    const attachLabel = document.getElementById("attachLabel");
    const fileInput = document.getElementById("fileInput");
    const inputs = {
      uni: document.getElementById("uni"),
      nation: document.getElementById("nation"),
      major: document.getElementById("major"),
      extra: document.getElementById("extra"),
    };
    const rUni = document.getElementById("rUni");
    const rNation = document.getElementById("rNation");
    const rMajor = document.getElementById("rMajor");
    const rExtra = document.getElementById("rExtra");
    const resetBtn = document.getElementById("resetBtn");

    function setFormat(fmt){
      pills.forEach(p => p.classList.toggle("active", p.dataset.fmt === fmt));
      attachLabel.textContent = `إرفاق ملفات CV (${fmt})`;
      const map = { PDF: ".pdf", XLSX: ".xlsx", CSV: ".csv" };
      fileInput.setAttribute("accept", map[fmt] || ".pdf");
      fileInput.value = "";
    }
    pills.forEach(p => p.addEventListener("click", () => setFormat(p.dataset.fmt)));
    setFormat("PDF");

    function refreshReview(){
      rUni.textContent   = inputs.uni.value    || "—";
      rNation.textContent= inputs.nation.value || "—";
      rMajor.textContent = inputs.major.value  || "—";
      rExtra.textContent = inputs.extra.value  || "—";
    }
    Object.values(inputs).forEach(inp => inp.addEventListener("input", refreshReview));
    refreshReview();

    resetBtn.addEventListener("click", () => {
      inputs.uni.value = "";
      inputs.nation.value = "";
      inputs.major.value = "";
      inputs.extra.value = "";
      setFormat("PDF");
      refreshReview();
    });
  </script>
</body>
</html>
"""

# نعرض واجهتك داخل ستريملت بارتفاع مناسب
components.html(html, height=1400, scrolling=True)
