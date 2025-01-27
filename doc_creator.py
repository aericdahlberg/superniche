for title, speaker, time, description in agenda_data:
    doc.add_heading(f'{time} - {title}', level=2)
    doc.add_paragraph(f'Speaker: {speaker}')
    doc.add_paragraph(description)