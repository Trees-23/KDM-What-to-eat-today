import type { Metadata, Viewport } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'RecipeRAG - 智能菜谱检索与问答',
  description: '基于 GraphRAG 的中文菜谱检索与烹饪问答系统',
  keywords: 'RecipeRAG,GraphRAG,菜谱检索,烹饪问答,食材',
  authors: [{ name: 'RecipeRAG' }],
}

export const viewport: Viewport = {
  width: 'device-width',
  initialScale: 1,
  themeColor: '#0ea5e9',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="zh-CN">
      <body className="antialiased">
        <div id="root">{children}</div>
        <div id="modal-root" />
        <div id="toast-root" />
      </body>
    </html>
  )
}
