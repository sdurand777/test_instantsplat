frame_height, frame_width, layers = images[0].shape
fps = 30  # Frames per second
output_video_file = 'output_video.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = cv2.VideoWriter(output_video_file, fourcc, fps, (frame_width, frame_height))
for img in images:  img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR); video_writer.write(img_bgr)
video_writer.release()
