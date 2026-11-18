import SwiftUI

struct Dashboard: View {
    let rows: [Row]
    var body: some View {
        ScrollView {
            VStack {
                ForEach(rows) { row in
                    HStack {
                        Circle().fill(.green).frame(width: 8, height: 8)
                        Text(row.title).font(.system(size: 15))
                    }
                }
            }
        }
        .background(LinearGradient(colors: [.purple, .indigo], startPoint: .top, endPoint: .bottom))
        .shadow(color: .purple, radius: 20)
        .navigationBarBackButtonHidden(true)
        .toolbar { Image(systemName: "line.3.horizontal") }
        .ignoresSafeArea()
        .overlay { Text("A").background(.ultraThinMaterial) }
        .safeAreaInset(edge: .top) { Text("B").background(.thinMaterial) }
        .toolbarBackground(.regularMaterial)
    }
}
