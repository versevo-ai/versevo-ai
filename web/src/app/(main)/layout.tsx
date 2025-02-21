export default function MainLayout({
  children
}: {
  children: React.ReactNode
}): React.JSX.Element {
  return (
    <main lang="en">
      {children}
    </main>
  )
}