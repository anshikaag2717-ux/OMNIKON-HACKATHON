function StudentDetail({ student, onBack }) {
  if (!student) {
    return null;
  }

  const riskClass = student.level.toLowerCase();

  return (
    <div className="student-detail-page">

      <button className="back-button" onClick={onBack}>
        ← Back to students
      </button>

      <div className="detail-header">
        <div>
          <p className="eyebrow">STUDENT PROFILE</p>
          <h1>{student.name}</h1>
          <p className="detail-id">{student.id}</p>
        </div>

        <span className={`risk-badge large ${riskClass}`}>
          <span></span>
          {student.level} Risk
        </span>
      </div>

      <div className="detail-grid">

        <section className="detail-card risk-summary">
          <p className="card-label">PREDICTED DROPOUT RISK</p>

          <div className={`risk-score ${riskClass}`}>
            {student.risk.toFixed(2)}%
          </div>

          <p className="card-description">
            Current predicted risk based on available student information.
          </p>
        </section>

        <section className="detail-card">
          <p className="card-label">STUDENT INFORMATION</p>

          <div className="info-grid">
            <div>
              <span>Department</span>
              <strong>{student.department}</strong>
            </div>

            <div>
              <span>Semester</span>
              <strong>{student.semester}</strong>
            </div>

            <div>
              <span>GPA</span>
              <strong>{student.gpa.toFixed(1)}</strong>
            </div>

            <div>
              <span>Attendance</span>
              <strong>{student.attendance}%</strong>
            </div>
          </div>
        </section>

      </div>

      <section className="detail-card factors-card">
        <div className="card-heading">
          <div>
            <p className="card-label">RISK FACTORS</p>
            <h2>Factors increasing risk</h2>
          </div>
        </div>

        <div className="factor-list">

          <div className="factor-item">
            <div className="factor-marker high"></div>
            <div>
              <strong>Low attendance</strong>
              <p>Attendance is contributing to the student's current risk.</p>
            </div>
            <span className="importance">Moderate</span>
          </div>

          <div className="factor-item">
            <div className="factor-marker high"></div>
            <div>
              <strong>Assignment delays</strong>
              <p>Delayed assignments are increasing the predicted risk.</p>
            </div>
            <span className="importance">Moderate</span>
          </div>

          <div className="factor-item">
            <div className="factor-marker high"></div>
            <div>
              <strong>GPA</strong>
              <p>Academic performance is contributing to the risk.</p>
            </div>
            <span className="importance">Moderate</span>
          </div>

          <div className="factor-item">
            <div className="factor-marker high"></div>
            <div>
              <strong>Stress level</strong>
              <p>Reported stress is contributing to the predicted risk.</p>
            </div>
            <span className="importance">Moderate</span>
          </div>

        </div>
      </section>

      <div className="detail-grid">

        <section className="detail-card">
          <p className="card-label">PROTECTIVE FACTORS</p>
          <h2>Factors reducing risk</h2>

          <div className="simple-factor">
            <span>✓</span>
            <div>
              <strong>Internet access</strong>
              <p>Access to internet resources is reducing risk.</p>
            </div>
          </div>

          <div className="simple-factor">
            <span>✓</span>
            <div>
              <strong>No part-time job</strong>
              <p>No additional employment commitment is currently reported.</p>
            </div>
          </div>
        </section>

        <section className="detail-card">
          <p className="card-label">RECOMMENDED ACTIONS</p>
          <h2>Suggested interventions</h2>

          <div className="recommendation">
            <div className="recommendation-icon">01</div>
            <div>
              <strong>Attendance intervention</strong>
              <p>
                Follow up with the student to identify barriers to regular
                attendance.
              </p>
            </div>
          </div>

          <div className="recommendation">
            <div className="recommendation-icon">02</div>
            <div>
              <strong>Academic mentoring</strong>
              <p>
                Provide targeted academic mentoring and subject-specific
                support.
              </p>
            </div>
          </div>

          <div className="recommendation">
            <div className="recommendation-icon">03</div>
            <div>
              <strong>Wellbeing support</strong>
              <p>
                Recommend appropriate counselling or student wellbeing
                resources.
              </p>
            </div>
          </div>

        </section>

      </div>

    </div>
  );
}

export default StudentDetail;