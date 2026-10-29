// Rendert eine Seite mit dem macOS-WebKit (wie Safari) und speichert sie als PNG.
// Aufruf: swift screenshot.swift <url> <ausgabe.png> <breite> <höhe>
import AppKit
import WebKit

let a = CommandLine.arguments
let url = URL(string: a[1])!, out = a[2]
let w = Double(a[3])!, h = Double(a[4])!

class D: NSObject, WKNavigationDelegate {
  func webView(_ v: WKWebView, didFinish n: WKNavigation!) {
    DispatchQueue.main.asyncAfter(deadline: .now() + 6) {   // iframes und Animationen fertig laden
      let c = WKSnapshotConfiguration(); c.snapshotWidth = NSNumber(value: w)
      v.takeSnapshot(with: c) { img, err in
        guard let img = img, let tiff = img.tiffRepresentation, let rep = NSBitmapImageRep(data: tiff),
              let png = rep.representation(using: .png, properties: [:]) else { print(err ?? "Fehler"); exit(1) }
        try! png.write(to: URL(fileURLWithPath: out)); exit(0)
      }
    }
  }
}
let app = NSApplication.shared
let win = NSWindow(contentRect: NSRect(x: 0, y: 0, width: w, height: h), styleMask: [.borderless], backing: .buffered, defer: false)
// Animationen aus (auch in den iframes), sonst bleiben Ringe im unsichtbaren Fenster leer
let cfg = WKWebViewConfiguration()
let css = "*,*::before,*::after{transition:none!important;animation-duration:0s!important}"
cfg.userContentController.addUserScript(WKUserScript(source: "document.addEventListener('DOMContentLoaded',()=>{const s=document.createElement('style');s.textContent='\(css)';document.head.appendChild(s)})", injectionTime: .atDocumentStart, forMainFrameOnly: false))
let v = WKWebView(frame: win.contentView!.bounds, configuration: cfg)
let d = D(); v.navigationDelegate = d
win.contentView!.addSubview(v)
v.load(URLRequest(url: url))
DispatchQueue.main.asyncAfter(deadline: .now() + 30) { print("Timeout"); exit(1) }
app.run()
