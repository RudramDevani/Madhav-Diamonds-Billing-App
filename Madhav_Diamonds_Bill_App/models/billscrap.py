def htmlcode(Bdt,bno,djl,qtyl,pl,tpl,gt, Bnm):
  import datetime
  date = f"{Bdt: %d-%m-%Y}"
  billno = bno
  
  DJ1 = DJ2 = DJ3 = DJ4 = DJ5 = DJ6 = DJ7 = DJ8 = DJ9 = ""
  Q1 = Q2 = Q3 = Q4 = Q5 = Q6 = Q7 = Q8 = Q9 = ""
  P1 = P2 = P3 = P4 = P5 = P6 = P7 = P8 = P9 = ""
  TP1 = TP2 = TP3 = TP4 = TP5 = TP6 = TP7 = TP8 = TP9 = 0.00

  desc = [DJ1, DJ2, DJ3, DJ4, DJ5, DJ6, DJ7, DJ8, DJ9]
  qty = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9]
  pricel = [P1, P2, P3, P4, P5, P6, P7, P8, P9]
  totalpricel = [TP1, TP2, TP3, TP4, TP5, TP6, TP7, TP8, TP9]

  for i1 in range(0, len(djl)):
      desc[i1] = djl[i1]
  for i2 in range(0, len(qtyl)):
      qty[i2] = qtyl[i2]
  for i3 in range(0, len(pl)):
      pricel[i3] = pl[i3]
  for i4 in range(0, len(tpl)):
      totalpricel[i4] = tpl[i4]

  Total = gt

  Adj=0.00

  billcode=f"""<!DOCTYPE html>
  <html lang="en">
  <head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Invoice {billno} - Mukeshbhai Dhirubhai Devani</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root{{
      --indigo:#283593;
      --name:#7468e0;
      --pan:#1a5fc9;
      --text:#000;
      --label:#444;
      --muted:#666;
      --faint:#999;
      --band:#f3f3f3;
      --pink:#e91e8c;
    }}
    *{{box-sizing:border-box;margin:0;padding:0}}
    body{{
      background:#e9e9e9;
      font-family:Roboto,Arial,Helvetica,sans-serif;
      color:var(--text);
      display:flex;justify-content:center;
      padding:20px 0;
      overflow-x:auto;
    }}
    /* A4 sheet: 794 x 1123 px */
    .page{{
      position:relative;
      width:794px;height:1123px;
      background:#fff;
      flex:none;
      box-shadow:0 2px 10px rgba(0,0,0,.2);
    }}
    .abs{{position:absolute;white-space:nowrap}}

    .bar{{left:76px;top:71px;width:642px;height:10px;background:var(--indigo)}}
    .name{{left:128px;top:105px;font-size:24px;line-height:30px;color:var(--name);font-weight:400}}
    .pan{{left:128px;top:142px;font-size:12.5px;line-height:18px;color:var(--pan);font-weight:700}}
    .addr{{left:128px;top:165px;font-size:12.5px;line-height:18px}}
    .title{{left:128px;top:193px;font-size:37px;line-height:46px;font-weight:700;color:var(--indigo)}}

    .lbl{{font-size:12.5px;line-height:18px;font-weight:700;color:var(--label)}}
    .val{{font-size:11.5px;line-height:18px;color:var(--muted)}}

    .divider{{left:124px;top:431px;width:546px;height:1px;background:#b7b7b7}}

    table{{
      position:absolute;left:124px;top:458px;width:546px;
      border-collapse:collapse;table-layout:fixed;
    }}
    col.c1{{width:250px}} col.c2{{width:82px}} col.c3{{width:104px}} col.c4{{width:110px}}
    th{{
      height:34px;font-size:12.5px;font-weight:700;color:var(--indigo);
      text-align:right;vertical-align:middle;padding:0;
    }}
    th:first-child{{text-align:left;padding-left:5px}}
    th:last-child{{padding-right:5px}}
    td{{
      height:26px;padding:0;vertical-align:middle;text-align:right;
      font-size:11.5px;color:var(--muted);
    }}
    td:first-child{{text-align:left;padding-left:5px;color:#000}}
    td:last-child{{padding-right:5px;color:var(--label)}}
    tbody tr:nth-child(odd){{background:var(--band)}}

    .line{{left:124px;top:726px;width:287px;height:1.5px;background:#000}}

    .k{{left:128px;font-size:11.5px;line-height:18px;color:var(--label)}}
    .v{{left:190px;font-size:11.5px;line-height:18px;color:var(--faint)}}

    .sl{{right:234px;font-size:11.5px;line-height:18px;color:var(--indigo);text-align:right}}
    .sv{{right:129px;font-size:11.5px;line-height:18px;font-weight:700;text-align:right}}
    .total{{right:129px;top:788px;font-size:24px;line-height:30px;font-weight:700;color:var(--pink);text-align:right}}

    @page{{size:A4;margin:0}}
    @media print{{
      body{{background:#fff;padding:0;display:block}}
      .page{{box-shadow:none;margin:0}}
      *{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
    }}
  </style>
  </head>
  <body>
  <div class="page">

    <div class="abs bar"></div>

    <div class="abs name">MUKESHBHAI DHIRUBHAI DEVANI</div>
    <div class="abs pan">PAN: AJCPD5391C</div>
    <div class="abs addr">21, Swaminarayan Nagar, Savani, Nr. Gitanjali, Varachha, Surat - 395006</div>
    <div class="abs title">Invoice</div>

    <div class="abs lbl" style="left:128px;top:292px">Invoice for</div>
    <div class="abs lbl" style="left:462px;top:292px">Invoice #</div>
    <div class="abs lbl" style="left:566px;top:292px">Date</div>

    <div class="abs val" style="left:128px;top:316px">{Bnm}</div>
    <div class="abs val" style="left:462px;top:316px">{billno}</div>
    <div class="abs val" style="left:566px;top:316px">{date}</div>

    <div class="abs lbl" style="left:128px;top:343px;font-size:13.5px">GSTN</div>
    <div class="abs val" style="left:322px;top:343px">24AAXFM9362Q1Z3</div>

    <div class="abs lbl" style="left:128px;top:364px;font-size:13.5px">ADDRESS</div>
    <div class="abs val" style="left:128px;top:388px">PLOT 1 to 5, KOHNOOR INDUSTRIAL ESTATE, VARACHHA SURAT - 395006</div>

    <div class="abs divider"></div>

    <table>
      <colgroup><col class="c1"><col class="c2"><col class="c3"><col class="c4"></colgroup>
      <thead>
        <tr><th>Description</th><th>Qty</th><th>Unit price</th><th>Total price</th></tr>
      </thead>
      <tbody>
        <tr><td>{desc[0]}</td><td>{qty[0]}</td><td>{pricel[0]}</td><td>₹{totalpricel[0]:.2f}</td></tr>
        <tr><td>{desc[1]}</td><td>{qty[1]}</td><td>{pricel[1]}</td><td>₹{totalpricel[1]:.2f}</td></tr>
        <tr><td>{desc[2]}</td><td>{qty[2]}</td><td>{pricel[2]}</td><td>₹{totalpricel[2]:.2f}</td></tr>
        <tr><td>{desc[3]}</td><td>{qty[3]}</td><td>{pricel[3]}</td><td>₹{totalpricel[3]:.2f}</td></tr>
        <tr><td>{desc[4]}</td><td>{qty[4]}</td><td>{pricel[4]}</td><td>₹{totalpricel[4]:.2f}</td></tr>
        <tr><td>{desc[5]}</td><td>{qty[5]}</td><td>{pricel[5]}</td><td>₹{totalpricel[5]:.2f}</td></tr>
        <tr><td>{desc[6]}</td><td>{qty[6]}</td><td>{pricel[6]}</td><td>₹{totalpricel[6]:.2f}</td></tr>
        <tr><td>{desc[7]}</td><td>{qty[7]}</td><td>{pricel[7]}</td><td>₹{totalpricel[7]:.2f}</td></tr>
        <tr><td>{desc[8]}</td><td>{qty[8]}</td><td>{pricel[8]}</td><td>₹{totalpricel[8]:.2f}</td></tr>
      </tbody>
    </table>

    <div class="abs line"></div>

    <div class="abs k" style="top:739px">NAME</div>
    <div class="abs v" style="top:739px">MUKESHBHAI DHIRUBHAI DEVANI</div>
    <div class="abs k" style="top:765px">BANK</div>
    <div class="abs v" style="top:765px">BANK OF BARODA</div>
    <div class="abs k" style="top:805px">A/C</div>
    <div class="abs v" style="top:805px">93330100036205</div>
    <div class="abs k" style="top:831px">IFSC</div>
    <div class="abs" style="left:190px;top:827px;font-size:11.5px;line-height:18px;color:#777">BARB0DBNVAR</div>

    <div class="abs sl" style="top:739px">Subtotal</div>
    <div class="abs sv" style="top:739px">₹{Total:.2f}</div>
    <div class="abs sl" style="top:765px">Adjustments</div>
    <div class="abs sv" style="top:765px">₹{Adj:.2f}</div>
    <div class="abs total">₹{Total:.2f}</div>

  </div>
  </body>
  </html>"""

  return billcode
