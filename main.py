import datetime
import requests

#--- Keys ---#
PUSHOVER_KEY = "um3e9ioxybhsekhzdjrh1c9hb12et7" # User specific info, change it to your own
PUSHOVER_TOKEN = "axgf7pwvytpq5rseo92bo1pgi36vvp" # For the app

#--- Workout Plan by Day, Separated ---#
GYMWORKOUTS = {
    "Monday": {
        "title": "Upper (Chest, Triceps, Shoulders)",
        "exercises":[
            "Rowers x30",
            "Pushups x40",
            "30 Minute Cardio Session (60/120s)",
            "Smith Machine Bench Press (4 x 6), inc weight",
            "Supine Bench Press (3 x 6), const weight",
            "Shoulder Press/Skull Crushers (3 x 8), medium weight",
            "Incline Bench Press (DB or Smith) (3 x 10,8,6), inc by 2.5",
            "Cable/Pec Fly (3 x 15), controlled",
            "OH Face Pulls (4 x 12), controlled",
            "Tricep Extensions (4 x 10)"
        ]
    },
    "Tuesday": {
        "title": "Back + Biceps",
        "exercises":[
            "Rowers x30",
            "Pushups x40",
            "30 Minute Cardio Sessions (Five Mins On, Five Mins Off)",
            "Lat Pulldowns (4 x 15), 60%, 1 set warmup",
            "Dumbbell Pullovers (2 x 15), controlled",
            "DB Rows (3 x 12), controlled (same weight as DBP)",
            "Preacher Curls (3 x 20), controlled",
            "Hammer Curls (4 x 12), 50%",
            "Seated Rows (4 x 12), 40%"
        ]
    },
    "Wednesday": {
        "title": "Legs (Quad Focus)",
        "exercises":[
            "High Knees 4 x 10",
            "Motivator 5 downward",
            "Squats (Smith Machine) 5 x 6, 80%",
            "Rear Lunges 4 x 10, last 2 sets 40% weights",
            "Leg Press 2 x 20, 70%",
            "Leg Extensions 4 x 12, 70%",
            "Leg Adductors 2 x 30, 60%",
            "Recovery: Bent Leg Body Twist, Thigh Stretch"
        ]
    },
    "Thursday":{
        "title": "Arms",
        "exercises":[
            "Spiderman Pushups 4 x 6",
            "Windmills 4 x 10, cadence",
            "Warm up 15 min run 15 mins",
            "Military Press 3x6, 3x5, 3x4, increase each time",
            "I-Y-T Raises 3 x 10 each",
            "Rope Curls 4 x 10",
            "OH Face Pull 2 x 24",
            "Overhead Tricep Extensions - Cable 4 x 10",
            "Tricep Pushdowns 4 x 10",
            "Shrugs 4x10, 4x8, 4x6, 4x4"
        ]
    },
    "Friday": {
        "title": "Legs (Glute/Hamstrings Focus) + Abdominals",
        "exercises":[
            "Air Squats 3 x 10",
            "Deadlifts (Smith Machine) - AFT weight",
            "Hip Thrusts 3 x 10",
            "Seated Leg Curls 3 x 12",
            "Leg Abductors 2 x 30, 60%",
            "Abdominal Crunches 3 x 10",
            "Rowers 3 x 10"
        ]
    },
    "Saturday": {
        "title": "Chest and Back (Isolated Movements)",
        "exercises": [
            "Iso Bench Press (Machine or DB) 4 sets of 8",
            "Single Arm Lat Pull-down 4 sets of 10",
            "Iso Incline Bench 3 sets of 8",
            "Iso Seated Row 3 sets of 10",
            "Cable Fly 4 sets of 10",
            "Lat Pullover 4 sets of 10",
            "Dips X Pull-ups Super set 3 sets til failure"
        ]
    },
    "Sunday": {
        "title": "Rest Day",
        "exercises": [
            "30 Min Cardio (3.5-3.7 Speed w 12 Incline or 6.0 Speed w 0 Incline)",
            "Abs Circuit (Planks, Ab Wheel, Hanging Leg Raises, Hanging Twist) 1 Min, 3 sets",
            "Active and Dynamic Stretching, Foam Roll for Recovery"
        ]
    }
}
def send_pushover_notification(title, message):
    """Sends a notification to your device via Pushover."""
    if PUSHOVER_KEY == "YOUR_USER_KEY" or PUSHOVER_TOKEN == "YOUR_API_TOKEN":
        print("ERROR: Please replace 'USER_KEY' and 'API_TOKEN' in the script.")
        return
    try:
        response = requests.post("https://api.pushover.net/1/messages.json", data={
            "token": PUSHOVER_TOKEN,
            "user": PUSHOVER_KEY,
            "title": title,
            "message": message,
            "priority": 0 # Normal priority
        })
        response.raise_for_status() # Raise an exception for bad status codes
        print("Notification sent successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {e}")
def main():
    # Get date as string and get current day workout
    day_workout=datetime.datetime.now().strftime("%A")
    workout_info = GYMWORKOUTS.get(day_workout)
    notification_title = f"Let's get this workout in broski. Time to grind."
    if workout_info:
        workout_title = workout_info["title"]
        exercises = workout_info["exercises"]
        
        # Build the message string with a title and a bulleted list of exercises
        message_lines = [workout_title]
        for exercise in exercises:
            message_lines.append(f"• {exercise}")
        
        workout_plan = "\n".join(message_lines)
    else:
        # Fallback message if today is not in the WORKOUTS dictionary
        workout_plan = "No workout scheduled for today."
        notification_title = "Rest Day"

    # Send the notification
    send_pushover_notification(notification_title, workout_plan)

if __name__ == "__main__":
    main()