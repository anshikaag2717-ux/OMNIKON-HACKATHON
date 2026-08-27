import { useMemo, useState } from "react";
import "./App.css";

const students = [
  {
    id: "STU001",
    name: "Aarav Sharma",
    department: "Computer Science",
    semester: 3,
    gpa: 1.8,
    attendance: 62,
    risk: 87.32,
    level: "High",
    lastUpdate: "Today",
  },
  {
    id: "STU002",
    name: "Priya Patel",
    department: "Information Technology",
    semester: 2,
    gpa: 3.1,
    attendance: 91,
    risk: 12.45,
    level: "Low",
    lastUpdate: "Today",
  },
  {
    id: "STU003",
    name: "Rohan Mehta",
    department: "Computer Science",
    semester: 4,
    gpa: 2.1,
    attendance: 74,
    risk: 64.18,
    level: "Medium",
    lastUpdate: "Yesterday",
  },
  {
    id: "STU004",
    name: "Ananya Singh",
    department: "Electronics",
    semester: 3,
    gpa: 2.4,
    attendance: 68,
    risk: 71.56,
    level: "High",
    lastUpdate: "Yesterday",
  },
  {
    id: "STU005",
    name: "Kabir Verma",
    department: "Mechanical",
    semester: 5,
    gpa: 3.4,
    attendance: 88,
    risk: 18.72,
    level: "Low",
    lastUpdate: "2 days ago",
  },
  {
    id: "STU006",
    name: "Meera Kapoor",
    department: "Information Technology",
    semester: 4,
    gpa: 2.7,
    attendance: 79,
    risk: 48.91,
    level: "Medium",
    lastUpdate: "2 days ago",
  },
];

function App() {
  const [search, setSearch] = useState("");
  const [riskFilter, setRiskFilter] = useState("All");

  const filteredStudents = useMemo(() => {
    return students.filter((student) => {
      const matchesSearch =
        student.name.toLowerCase().includes(search.toLowerCase()) ||
        student.id.toLowerCase().includes(search.toLowerCase());

      const matchesRisk =
        riskFilter === "All" || student.level === riskFilter;

      return matchesSearch && matchesRisk;
    });
  }, [search, riskFilter]);

  const totalStudents = students.length;
  const highRisk = students.filter((s) => s.level === "High").length;
  const mediumRisk = students.filter((s) => s.level === "Medium").length;
  const lowRisk = students.filter((s) => s.level === "Low").length;

  return (
    <div className="app">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-icon">EW</div>
          <div>
            <h2>EarlyWatch</h2>
            <span>Student Support</span>
          </div>
        </div>

        <nav className="navigation">
          <button className="nav-item active">
            <span>▦</span>
            Dashboard
          </button>

          <button className="nav-item">
            <span>◉</span>
            Students
          </button>

          <button className="nav-item">
            <span>◒</span>
            Analytics
          </button>

          <button className="nav-item">
            <span>✓</span>
            Interventions
          </button>
        </nav>

        <div className="sidebar-bottom">
          <div className="support-card">
            <span className="support-icon">?</span>
            <div>
              <strong>Need help?</strong>
              <p>Review intervention guidance</p>
            </div>
          </div>

          <div className="profile">
            <div className="avatar">JD</div>
            <div>
              <strong>Dr. Jordan Davis</strong>
              <span>Academic Advisor</span>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="main-content">
        <header className="topbar">
          <div>
            <p className="eyebrow">OVERVIEW</p>
            <h1>Student Early Warning</h1>
            <p className="subtitle">
              Monitor student risk and identify who may need support.
            </p>
          </div>

          <div className="topbar-actions">
            <button className="icon-button">⌕</button>
            <button className="notification-button">
              ♢
              <span></span>
            </button>
            <div className="top-avatar">JD</div>
          </div>
        </header>

        {/* Statistics */}
        <section className="stats-grid">
          <div className="stat-card">
            <div className="stat-top">
              <span>Total Students</span>
              <div className="stat-icon neutral">◉</div>
            </div>
            <strong>{totalStudents}</strong>
            <p>Currently monitored</p>
          </div>

          <div className="stat-card high-card">
            <div className="stat-top">
              <span>High Risk</span>
              <div className="stat-icon high">!</div>
            </div>
            <strong>{highRisk}</strong>
            <p>Require attention</p>
          </div>

          <div className="stat-card medium-card">
            <div className="stat-top">
              <span>Medium Risk</span>
              <div className="stat-icon medium">◐</div>
            </div>
            <strong>{mediumRisk}</strong>
            <p>Need monitoring</p>
          </div>

          <div className="stat-card low-card">
            <div className="stat-top">
              <span>Low Risk</span>
              <div className="stat-icon low">✓</div>
            </div>
            <strong>{lowRisk}</strong>
            <p>Currently stable</p>
          </div>
        </section>

        {/* Priority Banner */}
        <section className="priority-banner">
          <div className="priority-icon">!</div>
          <div>
            <strong>{highRisk} students require immediate attention</strong>
            <p>
              Review their risk factors and consider appropriate support
              interventions.
            </p>
          </div>
          <button>View high-risk students →</button>
        </section>

        {/* Students */}
        <section className="students-section">
          <div className="section-header">
            <div>
              <h2>Students requiring attention</h2>
              <p>Prioritized based on current predicted dropout risk.</p>
            </div>

            <button className="outline-button">Export</button>
          </div>

          <div className="toolbar">
            <div className="search-box">
              <span>⌕</span>
              <input
                type="text"
                placeholder="Search students or ID..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
              />
            </div>

            <select
              value={riskFilter}
              onChange={(e) => setRiskFilter(e.target.value)}
              className="filter-select"
            >
              <option value="All">All risk levels</option>
              <option value="High">High risk</option>
              <option value="Medium">Medium risk</option>
              <option value="Low">Low risk</option>
            </select>
          </div>

          <div className="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>STUDENT</th>
                  <th>DEPARTMENT</th>
                  <th>GPA</th>
                  <th>ATTENDANCE</th>
                  <th>RISK</th>
                  <th>STATUS</th>
                  <th>UPDATED</th>
                </tr>
              </thead>

              <tbody>
                {filteredStudents.map((student) => (
                  <tr key={student.id}>
                    <td>
                      <div className="student-cell">
                        <div className="student-avatar">
                          {student.name
                            .split(" ")
                            .map((word) => word[0])
                            .join("")}
                        </div>

                        <div>
                          <strong>{student.name}</strong>
                          <span>{student.id}</span>
                        </div>
                      </div>
                    </td>

                    <td>
                      <div className="department-cell">
                        <span>{student.department}</span>
                        <small>Semester {student.semester}</small>
                      </div>
                    </td>

                    <td>
                      <strong>{student.gpa.toFixed(1)}</strong>
                    </td>

                    <td>
                      <div className="attendance">
                        <div className="attendance-bar">
                          <div
                            style={{ width: `${student.attendance}%` }}
                          ></div>
                        </div>
                        <span>{student.attendance}%</span>
                      </div>
                    </td>

                    <td>
                      <strong className={`risk-number ${student.level.toLowerCase()}`}>
                        {student.risk.toFixed(2)}%
                      </strong>
                    </td>

                    <td>
                      <span className={`risk-badge ${student.level.toLowerCase()}`}>
                        <span></span>
                        {student.level}
                      </span>
                    </td>

                    <td>
                      <span className="updated">{student.lastUpdate}</span>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>

            {filteredStudents.length === 0 && (
              <div className="empty-state">
                No students found matching your search.
              </div>
            )}
          </div>

          <div className="table-footer">
            <span>
              Showing {filteredStudents.length} of {totalStudents} students
            </span>

            <div className="pagination">
              <button disabled>←</button>
              <button className="current-page">1</button>
              <button>2</button>
              <button>3</button>
              <button>→</button>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;