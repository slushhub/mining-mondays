// The same test with javascript

function acceptMeetingRequest(meetingRequestId, meetingTimeId, userId) {
  const userHasPermission = checkPermission(meetingRequestId, userId);

  if (userHasPermission) {
    const meetingAreaCategory = getMeetingAreaFromDatabase(meetingRequestId);

    if (meetingAreaCategory === 'meeting-tables') {
      reserveMeetingTable(meetingTimeId, userId);
    }

    updateMeetingRequestStatusToAccepted(meetingRequestId, userId);

    const updatedMeetingRequest = getMeetingRequestFromDatabase(
      meetingRequestId
    );

    return updatedMeetingRequest;
  }
}
