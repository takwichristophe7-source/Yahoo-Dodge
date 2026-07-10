-- Row Level Security Policies for Yahoo Dodge

-- ============================================
-- USERS TABLE POLICIES
-- ============================================

-- Users can read their own profile
CREATE POLICY "Users can read own profile"
    ON users FOR SELECT
    USING (auth.uid() = id OR is_admin = TRUE);

-- Users can update their own profile
CREATE POLICY "Users can update own profile"
    ON users FOR UPDATE
    USING (auth.uid() = id)
    WITH CHECK (auth.uid() = id);

-- Admins can read all users
CREATE POLICY "Admins can read all users"
    ON users FOR SELECT
    USING (is_admin = TRUE);

-- ============================================
-- LESSONS TABLE POLICIES
-- ============================================

-- Anyone can read published lessons
CREATE POLICY "Anyone can read published lessons"
    ON lessons FOR SELECT
    USING (is_published = TRUE);

-- Admins can read all lessons
CREATE POLICY "Admins can read all lessons"
    ON lessons FOR SELECT
    USING (is_admin = TRUE);

-- Admins can create lessons
CREATE POLICY "Admins can create lessons"
    ON lessons FOR INSERT
    WITH CHECK (is_admin = TRUE);

-- Admins can update lessons
CREATE POLICY "Admins can update lessons"
    ON lessons FOR UPDATE
    USING (is_admin = TRUE);

-- ============================================
-- USER LESSON PROGRESS POLICIES
-- ============================================

-- Users can read their own progress
CREATE POLICY "Users can read own lesson progress"
    ON user_lesson_progress FOR SELECT
    USING (auth.uid() = user_id);

-- Users can insert their own progress
CREATE POLICY "Users can insert own lesson progress"
    ON user_lesson_progress FOR INSERT
    WITH CHECK (auth.uid() = user_id);

-- Users can update their own progress
CREATE POLICY "Users can update own lesson progress"
    ON user_lesson_progress FOR UPDATE
    USING (auth.uid() = user_id);

-- ============================================
-- QUIZ RESULTS POLICIES
-- ============================================

-- Users can read their own quiz results
CREATE POLICY "Users can read own quiz results"
    ON quiz_results FOR SELECT
    USING (auth.uid() = user_id);

-- Users can insert their own quiz results
CREATE POLICY "Users can insert own quiz results"
    ON quiz_results FOR INSERT
    WITH CHECK (auth.uid() = user_id);

-- ============================================
-- SCAM REPORTS POLICIES
-- ============================================

-- Users can read approved scam reports
CREATE POLICY "Users can read approved reports"
    ON scam_reports FOR SELECT
    USING (is_approved = TRUE OR auth.uid() = user_id);

-- Users can insert scam reports
CREATE POLICY "Users can insert scam reports"
    ON scam_reports FOR INSERT
    WITH CHECK (auth.uid() = user_id);

-- Users can update their own reports (before approval)
CREATE POLICY "Users can update own reports"
    ON scam_reports FOR UPDATE
    USING (auth.uid() = user_id AND is_approved = FALSE);

-- Admins can read all reports
CREATE POLICY "Admins can read all reports"
    ON scam_reports FOR SELECT
    USING (is_admin = TRUE);

-- Admins can update reports
CREATE POLICY "Admins can update reports"
    ON scam_reports FOR UPDATE
    USING (is_admin = TRUE);

-- ============================================
-- NOTIFICATIONS POLICIES
-- ============================================

-- Users can read their own notifications
CREATE POLICY "Users can read own notifications"
    ON notifications FOR SELECT
    USING (auth.uid() = user_id);

-- Users can update their own notifications
CREATE POLICY "Users can update own notifications"
    ON notifications FOR UPDATE
    USING (auth.uid() = user_id);

-- System can insert notifications
CREATE POLICY "System can insert notifications"
    ON notifications FOR INSERT
    WITH CHECK (TRUE);

-- ============================================
-- LEADERBOARD POLICIES
-- ============================================

-- Anyone can read leaderboard
CREATE POLICY "Anyone can read leaderboard"
    ON leaderboard FOR SELECT
    USING (TRUE);

-- System can update leaderboard
CREATE POLICY "System can update leaderboard"
    ON leaderboard FOR UPDATE
    USING (TRUE);

-- ============================================
-- CERTIFICATES POLICIES
-- ============================================

-- Users can read their own certificates
CREATE POLICY "Users can read own certificates"
    ON certificates FOR SELECT
    USING (auth.uid() = user_id);

-- System can insert certificates
CREATE POLICY "System can insert certificates"
    ON certificates FOR INSERT
    WITH CHECK (TRUE);

-- ============================================
-- ENABLE RLS ON ALL TABLES
-- ============================================

ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE lessons ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_lesson_progress ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_questions ENABLE ROW LEVEL SECURITY;
ALTER TABLE quiz_results ENABLE ROW LEVEL SECURITY;
ALTER TABLE scam_reports ENABLE ROW LEVEL SECURITY;
ALTER TABLE phone_reports ENABLE ROW LEVEL SECURITY;
ALTER TABLE certificates ENABLE ROW LEVEL SECURITY;
ALTER TABLE notifications ENABLE ROW LEVEL SECURITY;
ALTER TABLE leaderboard ENABLE ROW LEVEL SECURITY;
ALTER TABLE badges ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_badges ENABLE ROW LEVEL SECURITY;
ALTER TABLE trending_scams ENABLE ROW LEVEL SECURITY;
