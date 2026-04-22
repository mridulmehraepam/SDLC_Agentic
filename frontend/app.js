const state = {
  episodes: [
    {
      id: 1,
      title: 'Future of AI in Podcasting',
      topic: 'AI & Media',
      duration: 45,
      date: '2026-05-02',
      tone: 'Professional',
      status: 'Draft',
      guests: ['Aditi Sharma'],
      outline: '1. Intro\n2. AI trends\n3. Guest insights\n4. Outro',
      script: ''
    },
    {
      id: 2,
      title: 'Building Better Founder Stories',
      topic: 'Storytelling',
      duration: 35,
      date: '2026-05-10',
      tone: 'Storytelling',
      status: 'Scripted',
      guests: ['Rohit Sinha', 'Mira Das'],
      outline: '1. Hook\n2. Founder journey\n3. Learnings\n4. CTA',
      script: 'Welcome to today\'s episode...'
    }
  ],
  selectedEpisodeId: null,
  aiHistory: [],
};

const $ = (id) => document.getElementById(id);

const dashboardView = $('dashboardView');
const workspaceView = $('workspaceView');
const guestsView = $('guestsView');
const episodeList = $('episodeList');
const guestsLibrary = $('guestsLibrary');
const searchInput = $('searchInput');
const statusFilter = $('statusFilter');

function showToast(message) {
  const toast = $('toast');
  toast.textContent = message;
  toast.classList.remove('hidden');
  setTimeout(() => toast.classList.add('hidden'), 1800);
}

function switchView(view) {
  [dashboardView, workspaceView, guestsView].forEach((v) => v.classList.remove('active'));
  document.querySelectorAll('.nav-btn').forEach((btn) => btn.classList.remove('active'));

  if (view === 'dashboard') dashboardView.classList.add('active');
  if (view === 'workspace') workspaceView.classList.add('active');
  if (view === 'guests') guestsView.classList.add('active');

  const activeBtn = document.querySelector(`.nav-btn[data-view="${view}"]`);
  if (activeBtn) activeBtn.classList.add('active');
}

function filteredEpisodes() {
  const search = searchInput.value.trim().toLowerCase();
  const status = statusFilter.value;
  return state.episodes.filter((episode) => {
    const searchMatch = !search || episode.title.toLowerCase().includes(search) || episode.topic.toLowerCase().includes(search);
    const statusMatch = status === 'all' || episode.status === status;
    return searchMatch && statusMatch;
  });
}

function renderEpisodeList() {
  const episodes = filteredEpisodes();
  if (!episodes.length) {
    episodeList.innerHTML = '<div class="empty-state"><h2>No episodes found</h2><p>Try changing filters or create a new episode.</p></div>';
    return;
  }

  episodeList.innerHTML = episodes
    .map(
      (episode) => `
      <article class="episode-card">
        <div class="episode-card-head">
          <strong>${episode.title}</strong>
          <span class="status-badge">${episode.status}</span>
        </div>
        <div>Topic: ${episode.topic} • ${episode.duration} mins • ${episode.date}</div>
        <div>Guests: ${episode.guests.join(', ') || 'None'}</div>
        <div class="actions">
          <button class="btn" data-open="${episode.id}">Open Workspace</button>
        </div>
      </article>
    `
    )
    .join('');

  document.querySelectorAll('[data-open]').forEach((btn) => {
    btn.addEventListener('click', () => {
      const id = Number(btn.getAttribute('data-open'));
      openEpisode(id);
      switchView('workspace');
    });
  });
}

function renderGuestsLibrary() {
  const uniqueGuests = [...new Set(state.episodes.flatMap((episode) => episode.guests))];
  guestsLibrary.innerHTML = uniqueGuests.length
    ? uniqueGuests.map((guest) => `<div class="guest-item">${guest}</div>`).join('')
    : '<p>No guests added yet.</p>';
}

function getSelectedEpisode() {
  return state.episodes.find((episode) => episode.id === state.selectedEpisodeId) || null;
}

function openEpisode(id) {
  state.selectedEpisodeId = id;
  renderWorkspace();
}

function renderWorkspace() {
  const empty = $('workspaceEmpty');
  const content = $('workspaceContent');
  const episode = getSelectedEpisode();

  if (!episode) {
    empty.classList.remove('hidden');
    content.classList.add('hidden');
    return;
  }

  empty.classList.add('hidden');
  content.classList.remove('hidden');

  $('workspaceTitle').textContent = `${episode.title}`;
  $('workspaceStatus').textContent = episode.status;

  $('titleInput').value = episode.title;
  $('topicInput').value = episode.topic;
  $('durationInput').value = episode.duration;
  $('dateInput').value = episode.date;
  $('toneInput').value = episode.tone;
  $('outlineInput').value = episode.outline;
  $('scriptInput').value = episode.script;

  $('guestTags').innerHTML = episode.guests.map((guest) => `<span class="guest-tag">${guest}</span>`).join('');
  $('aiHistory').innerHTML = state.aiHistory.map((item) => `<li>${item}</li>`).join('');
}

function saveWorkspaceFields() {
  const episode = getSelectedEpisode();
  if (!episode) return;

  episode.title = $('titleInput').value.trim() || episode.title;
  episode.topic = $('topicInput').value.trim();
  episode.duration = Number($('durationInput').value || 0);
  episode.date = $('dateInput').value;
  episode.tone = $('toneInput').value;
  episode.outline = $('outlineInput').value;
  episode.script = $('scriptInput').value;
}

function fakeAiGenerate(type) {
  const episode = getSelectedEpisode();
  if (!episode) {
    showToast('Select an episode first');
    return;
  }

  const prompt = $('promptInput').value.trim();
  if (!prompt) {
    showToast('Enter an AI prompt first');
    return;
  }

  $('aiStatus').textContent = `Generating ${type}...`;

  setTimeout(() => {
    if (type === 'outline') {
      const outline = `1) Hook for ${episode.title}\n2) Topic deep dive: ${episode.topic}\n3) Guest insights\n4) Key takeaways\n5) Outro`;
      $('outlineInput').value = outline;
      episode.outline = outline;
    }

    if (type === 'script') {
      const script = `Intro:\nWelcome back! Today we explore ${episode.topic}.\n\nMain:\nWe discuss key trends, practical insights, and examples.\n\nGuest Segment:\nOur guest shares real-world experiences.\n\nOutro:\nThanks for listening. Subscribe for more.`;
      $('scriptInput').value = script;
      episode.script = script;
    }

    const log = `${new Date().toLocaleTimeString()} - ${type} generated`;
    state.aiHistory.unshift(log);
    state.aiHistory = state.aiHistory.slice(0, 10);
    $('aiStatus').textContent = `${type} generated successfully.`;
    renderWorkspace();
  }, 900);
}

function createEpisode() {
  const nextId = Math.max(0, ...state.episodes.map((episode) => episode.id)) + 1;
  const newEpisode = {
    id: nextId,
    title: `New Episode ${nextId}`,
    topic: 'Untitled Topic',
    duration: 30,
    date: new Date().toISOString().split('T')[0],
    tone: 'Professional',
    status: 'Draft',
    guests: [],
    outline: '',
    script: '',
  };

  state.episodes.unshift(newEpisode);
  renderEpisodeList();
  renderGuestsLibrary();
  openEpisode(newEpisode.id);
  switchView('workspace');
  showToast('New episode created');
}

function addGuestToEpisode() {
  const episode = getSelectedEpisode();
  if (!episode) return;
  const guestName = $('guestInput').value.trim();
  if (!guestName) return;
  if (!episode.guests.includes(guestName)) episode.guests.push(guestName);
  $('guestInput').value = '';
  renderWorkspace();
  renderGuestsLibrary();
}

document.querySelectorAll('.nav-btn').forEach((btn) => {
  btn.addEventListener('click', () => switchView(btn.getAttribute('data-view')));
});

searchInput.addEventListener('input', renderEpisodeList);
statusFilter.addEventListener('change', renderEpisodeList);
$('newEpisodeBtn').addEventListener('click', createEpisode);
$('addGuestBtn').addEventListener('click', addGuestToEpisode);

$('saveDraftBtn').addEventListener('click', () => {
  saveWorkspaceFields();
  const episode = getSelectedEpisode();
  episode.status = 'Draft';
  renderWorkspace();
  renderEpisodeList();
  showToast('Draft saved');
});

$('saveVersionBtn').addEventListener('click', () => {
  saveWorkspaceFields();
  showToast('Script version saved');
});

$('markReadyBtn').addEventListener('click', () => {
  saveWorkspaceFields();
  const episode = getSelectedEpisode();
  episode.status = 'Scripted';
  renderWorkspace();
  renderEpisodeList();
  showToast('Episode marked ready');
});

$('generateOutlineBtn').addEventListener('click', () => fakeAiGenerate('outline'));
$('generateScriptBtn').addEventListener('click', () => fakeAiGenerate('script'));
$('regenerateBtn').addEventListener('click', () => {
  const prefer = $('scriptInput').value.trim() ? 'script' : 'outline';
  fakeAiGenerate(prefer);
});

renderEpisodeList();
renderGuestsLibrary();
renderWorkspace();
