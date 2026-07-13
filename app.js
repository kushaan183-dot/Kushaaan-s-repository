function parseLinesToObjects(lines, type) {
  return lines
    .map(l => l.trim())
    .filter(Boolean)
    .map(line => {
      const parts = line.split('|').map(p => p.trim())
      if (type === 'experience') {
        return { role: parts[0] || '', company: parts[1] || '', dates: parts[2] || '', details: parts[3] || '' }
      }
      if (type === 'education') {
        return { degree: parts[0] || '', school: parts[1] || '', dates: parts[2] || '' }
      }
      return line
    })
}

async function renderPreview(payload) {
  const res = await fetch('/preview', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) })
  const html = await res.text()
  document.getElementById('preview').innerHTML = html
}

document.getElementById('preview-btn').addEventListener('click', () => {
  const form = document.getElementById('resume-form')
  const fd = new FormData(form)
  const payload = {
    name: fd.get('name') || '',
    title: fd.get('title') || '',
    email: fd.get('email') || '',
    phone: fd.get('phone') || '',
    linkedin: fd.get('linkedin') || '',
    summary: fd.get('summary') || '',
    experiences: parseLinesToObjects(fd.get('experiences').split('\n'), 'experience'),
    education: parseLinesToObjects(fd.get('education').split('\n'), 'education'),
    skills: (fd.get('skills') || '').split('\n').map(s => s.trim()).filter(Boolean)
  }
  renderPreview(payload)
})

document.getElementById('reset-btn').addEventListener('click', () => {
  document.getElementById('resume-form').reset()
})

// Auto-preview sample on load
window.addEventListener('load', () => document.getElementById('preview-btn').click())
