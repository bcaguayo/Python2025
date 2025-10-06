from fpdf import FPDF
import random

# Define the bingo card content
cards = [
    "Has a favorite TV show or movie they rewatch",
    "Can play a musical instrument",
    "Likes to cook or bake",
    "Has met a celebrity or famous person",
    "Has watched a whole season of a show in one weekend",
    "Likes outdoor activities (hiking, biking, etc.)",
    "Likes water activities (swimming, kayaking, etc.)",
    "Has a unique collection (e.g., stamps, sneakers)",
    "Has traveled to more than three countries",
    "Speaks two languages or more",
    "Has a pet",
    "Enjoys board games or puzzles",
    "Has run a marathon or half-marathon",
    "Has read more than 3 books this year",
    "Has volunteered for a charity or cause",
    "Has tried a new hobby recently",
    "Has made something crafty or artistic",
    "Knows how to knit or crochet",
    "Has been on a road trip",
    "Has attended a live concert or show in the last year",
    "Can whistle a tune",
    "Has baked bread from scratch",
    "Has taken a dance class",
    "Has gone camping",
    "Has a signature dish they love to make",
    "Prefers tea over coffee",
    "Likes pineapple on pizza",
    "Has a tattoo",
    "Is left-handed"
]

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)
numPages = 30

# Add a page for each bingo card
for page_num in range(1, numPages + 1):
    pdf.set_text_color(0, 0, 0)
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Casual & Fun Mingle Bingo", ln=True, align='C')
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 8, "Please complete all items by writing a name under the prompt.", ln=True, align='C')
    pdf.ln(20)
    pdf.cell(0, 8, "Find someone who...", ln=True, align='C')
    pdf.ln(10)

    selected_items = random.sample(cards, 9)
    cell_width = 60
    cell_height = 10

    start_x = 15
    start_y = pdf.get_y()
    offset_y = [10, 50, 90]

    # Make a grid for 9 items
    pdf.set_line_width(0.5)
    pdf.line(start_x + 60, pdf.get_y(), start_x + 60, pdf.get_y() + 180)
    pdf.line(start_x + 120, pdf.get_y(), start_x + 120, pdf.get_y() + 180)
    pdf.line(start_x, pdf.get_y() + 60, start_x + 180, pdf.get_y() + 60)
    pdf.line(start_x, pdf.get_y() + 120, start_x + 180, pdf.get_y() + 120)    

    for row in range(3):
        for col in range(3):                
            x = start_x + col * cell_width
            y = start_y + row * cell_height * 2 + offset_y[row]
            pdf.set_xy(x, y)
            if row == 1 and col == 1 :
                pdf.multi_cell(cell_width, cell_height, "Free Space", border=0, align='C')
            else :
                pdf.multi_cell(cell_width, cell_height, selected_items[row * 3 + col], border=0, align='C')

    pdf.ln(50)
    pdf.set_font("Arial", '', 8)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 8, "Brought to you by the MI Team", ln=True, align='C')    

# Save the PDF
pdf.output("casual_fun_mingle_bingo_cards.pdf")
