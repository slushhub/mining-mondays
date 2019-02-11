"""
Test your skillz!
"""

# 1) What does this function do?
# 2) What happens if meeting area category is 'meeting-tables'
# 3) What does this function return?

def accept_meeting_request(meeting_request_id, meeting_time_id, user_id):

  user_has_permission = check_permission(meeting_request_id, user_id)

  if user_has_permission:

    meeting_area_category = get_meeting_area_category_from_database(meeting_request_id)

    if meeting_area_category == 'meeting-tables':

      reserve_meeting_table(meeting_time_id, user_id)

    update_meeting_request_status_to_accepted(meeting_request_id, user_id)

    updated_meeting_request = get_meeting_request_from_database(meeting_request_id)

    return updated_meeting_request
