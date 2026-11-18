import SwiftUI

struct Dashboard: View {
    let rows: [Row]
    var body: some View {
        List(rows) { row in
            Label(row.title, systemImage: row.symbol)
                .font(.body)
        }
        .background(Color(.systemGroupedBackground).ignoresSafeArea())
        .shadow(color: .black.opacity(0.1), radius: 4, y: 2)
    }
}
