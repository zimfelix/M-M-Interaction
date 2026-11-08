// Fasst eine A4-PDF zu Doppelseiten zusammen: S. 1+2, 3+4, … nebeneinander auf einem Blatt (A3 quer).
// Aufruf: swift doppelseiten.swift <eingabe.pdf> <ausgabe.pdf>
import CoreGraphics
import Foundation

let args = CommandLine.arguments
guard args.count == 3, let src = CGPDFDocument(URL(fileURLWithPath: args[1]) as CFURL),
      let first = src.page(at: 1) else { fatalError("Aufruf: swift doppelseiten.swift ein.pdf aus.pdf") }
let a4 = first.getBoxRect(.mediaBox)
var sheet = CGRect(x: 0, y: 0, width: a4.width * 2, height: a4.height)
let ctx = CGContext(URL(fileURLWithPath: args[2]) as CFURL, mediaBox: &sheet, nil)!
var n = 1
while n <= src.numberOfPages {
    ctx.beginPDFPage(nil)
    for (i, nr) in [n, n + 1].enumerated() where nr <= src.numberOfPages {
        ctx.saveGState()
        ctx.translateBy(x: CGFloat(i) * a4.width, y: 0)
        ctx.drawPDFPage(src.page(at: nr)!)
        ctx.restoreGState()
    }
    ctx.endPDFPage()
    n += 2
}
ctx.closePDF()
