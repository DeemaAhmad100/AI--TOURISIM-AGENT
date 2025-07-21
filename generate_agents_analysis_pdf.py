#!/usr/bin/env python3
"""
🔄 AI Agents Analysis PDF Generator
Converts the comprehensive AI agents analysis to a professional PDF document
"""

import os
import datetime
from pathlib import Path
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import re

def create_ai_agents_analysis_pdf():
    """Generate professional PDF of AI Agents Analysis"""
    
    try:
        # File paths
        base_path = Path(__file__).parent
        markdown_file = base_path / "AI_AGENTS_IN_DEPTH_ANALYSIS.md"
        pdf_file = base_path / "AI_Agents_In_Depth_Analysis.pdf"
        
        # Read markdown content
        if not markdown_file.exists():
            print(f"❌ Markdown file not found: {markdown_file}")
            return False
            
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create PDF document
        doc = SimpleDocTemplate(
            str(pdf_file), 
            pagesize=A4,
            rightMargin=72, 
            leftMargin=72,
            topMargin=72, 
            bottomMargin=50
        )
        
        # Define styles
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=colors.navy,
            fontName='Helvetica-Bold'
        )
        
        subtitle_style = ParagraphStyle(
            'CustomSubtitle',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=20,
            alignment=TA_CENTER,
            textColor=colors.darkblue,
            fontName='Helvetica'
        )
        
        heading1_style = ParagraphStyle(
            'CustomHeading1',
            parent=styles['Heading1'],
            fontSize=18,
            spaceAfter=15,
            spaceBefore=20,
            textColor=colors.darkblue,
            fontName='Helvetica-Bold'
        )
        
        heading2_style = ParagraphStyle(
            'CustomHeading2',
            parent=styles['Heading2'], 
            fontSize=14,
            spaceAfter=12,
            spaceBefore=15,
            textColor=colors.darkgreen,
            fontName='Helvetica-Bold'
        )
        
        heading3_style = ParagraphStyle(
            'CustomHeading3',
            parent=styles['Heading3'],
            fontSize=12,
            spaceAfter=10,
            spaceBefore=12,
            textColor=colors.darkorange,
            fontName='Helvetica-Bold'
        )
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=8,
            alignment=TA_JUSTIFY,
            fontName='Helvetica'
        )
        
        code_style = ParagraphStyle(
            'Code',
            parent=styles['Normal'],
            fontSize=9,
            fontName='Courier',
            backgroundColor=colors.lightgrey,
            leftIndent=20,
            rightIndent=20,
            spaceBefore=5,
            spaceAfter=5
        )
        
        # Build PDF content
        story = []
        
        # Parse markdown and convert to PDF elements
        lines = content.split('\n')
        current_section = []
        in_code_block = False
        code_block_content = []
        
        for line in lines:
            line = line.strip()
            
            # Handle code blocks
            if line.startswith('```'):
                if in_code_block:
                    # End code block
                    if code_block_content:
                        code_text = '\n'.join(code_block_content)
                        story.append(Paragraph(code_text, code_style))
                        story.append(Spacer(1, 10))
                    code_block_content = []
                    in_code_block = False
                else:
                    # Start code block
                    in_code_block = True
                continue
            
            if in_code_block:
                code_block_content.append(line)
                continue
            
            # Skip empty lines
            if not line:
                if current_section:
                    story.append(Spacer(1, 6))
                continue
            
            # Main title
            if line.startswith('# 🤖 **In-Depth Analysis'):
                story.append(Paragraph("🤖 In-Depth Analysis of AI Agents", title_style))
                story.append(Paragraph("AI Travel Platform Agent Architecture", subtitle_style))
                story.append(Spacer(1, 20))
                continue
            
            # Level 1 headers
            if line.startswith('## '):
                header_text = re.sub(r'^##\s*\*\*?|\*\*?$', '', line)
                header_text = re.sub(r'🔄|📋|🏗️|💡|👤|🔒|📈|📚', '', header_text).strip()
                story.append(Paragraph(header_text, heading1_style))
                continue
            
            # Level 2 headers
            if line.startswith('### '):
                header_text = re.sub(r'^###\s*\*\*?|\*\*?$', '', line)
                header_text = re.sub(r'✅|⚠️|🎯|🧠|🎭|🌍|🌤️', '', header_text).strip()
                story.append(Paragraph(header_text, heading2_style))
                continue
            
            # Level 3 headers
            if line.startswith('#### '):
                header_text = re.sub(r'^####\s*\*\*?|\*\*?$', '', line)
                header_text = re.sub(r'✅|⚠️|🎯|🧠|🎭|🌍|🌤️', '', header_text).strip()
                story.append(Paragraph(header_text, heading3_style))
                continue
            
            # Skip markdown decorations and separators
            if line.startswith('---') or line.startswith('*') and len(line) > 50:
                story.append(Spacer(1, 15))
                continue
            
            # Handle lists
            if line.startswith('- ') or line.startswith('* '):
                list_text = re.sub(r'^[-*]\s*', '• ', line)
                list_text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', list_text)
                list_text = re.sub(r'✅|❌|⚠️|🎯|📊|💰|🌍|🏨|🍽️|✈️', '', list_text)
                story.append(Paragraph(list_text, body_style))
                continue
            
            # Handle regular paragraphs
            if line and not line.startswith('#'):
                # Clean up markdown formatting
                clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                clean_line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', clean_line)
                clean_line = re.sub(r'`(.*?)`', r'<font name="Courier">\1</font>', clean_line)
                
                # Remove emojis for PDF
                clean_line = re.sub(r'[🔄📋🏗️💡👤🔒📈📚✅❌⚠️🎯📊💰🌍🏨🍽️✈️🧠🎭🌤️🔥⭐🚀💎🌟]', '', clean_line)
                
                if clean_line.strip():
                    story.append(Paragraph(clean_line, body_style))
        
        # Add document info
        story.insert(0, Spacer(1, 20))
        
        # Footer information
        story.append(PageBreak())
        story.append(Paragraph("Document Information", heading2_style))
        story.append(Paragraph(f"Generated: {datetime.datetime.now().strftime('%B %d, %Y at %I:%M %p')}", body_style))
        story.append(Paragraph("Platform: AI Travel Platform", body_style))
        story.append(Paragraph("Version: 1.0", body_style))
        story.append(Paragraph("Classification: Technical Documentation", body_style))
        
        # Build the PDF
        print("📄 Generating AI Agents Analysis PDF...")
        doc.build(story)
        
        print(f"✅ PDF generated successfully: {pdf_file}")
        print(f"📊 File size: {pdf_file.stat().st_size / 1024:.1f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ Error generating PDF: {str(e)}")
        return False

def main():
    """Main execution"""
    print("🤖 AI Agents Analysis PDF Generator")
    print("=" * 50)
    
    success = create_ai_agents_analysis_pdf()
    
    if success:
        print("\n🎉 SUCCESS!")
        print("📄 Professional PDF report generated")
        print("🚀 Ready for presentations and documentation")
    else:
        print("\n❌ FAILED!")
        print("🔧 Check error messages above")

if __name__ == "__main__":
    main()
