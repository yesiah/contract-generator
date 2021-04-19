import pathlib
from fpdf import FPDF

root_path = pathlib.Path(__file__).parent.absolute()

# trade by trade
# prepayment
# bi-weekly
# monthly
def trade_by_trade(self):
    path = root_path / "contract-templates/cht/逐筆結.txt"
    with open(path, 'rb') as f:
        txt = f.read().decode('UTF-8')
        self.set_text_color(r=0.0, g=100.0, b=0.0)
        self.set_font(family='AppleLiGothic', size=12)

        self.multi_cell(w=0, h=5, txt=txt)

def append_payment_method(self, payment_method):
    return trade_by_trade(self)

def titles(self):
    self.set_xy(0.0, 0.0)
    self.set_font('AppleLiGothic', '', 16)
    self.set_text_color(220, 50, 50)
    self.cell(w=210.0, h=40.0, align='C', txt="合約")

def texts(self, txt):
    self.set_xy(x=10.0, y=30.0)
    self.set_text_color(r=0.0, g=0.0, b=0.0)
    self.set_font(family='AppleLiGothic', size=12)
    self.multi_cell(w=0, h=5, txt=txt)

def generate(txt):
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("AppleLiGothic", "", "AppleLiGothic-Medium.ttf", uni=True) 
    titles(pdf)
    texts(pdf, txt)

    append_payment_method(pdf, "")

    pdf.output('tuto1.pdf', 'F')
