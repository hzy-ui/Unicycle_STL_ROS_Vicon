import rospy

if __name__ == "__main__":

    rospy.init_node("set_param")

    #  vehicle_postion
    rospy.set_param("pos_x",0);     rospy.set_param("pos_y",0)

    #  goal_postion
    rospy.set_param("goal_count",3)

    rospy.set_param("goal1_x",4);   rospy.set_param("goal1_y",3)
    rospy.set_param("goal2_x",0);   rospy.set_param("goal2_y",4)
    rospy.set_param("goal3_x",4);   rospy.set_param("goal3_y",0)


    #  goal_time_limition
    rospy.set_param("goal1_start",0);   rospy.set_param("goal1_end",30);    rospy.set_param("goal1_expect",27)

    rospy.set_param("goal2_start",30);  rospy.set_param("goal2_end",50);    rospy.set_param("goal2_expect",47)

    rospy.set_param("goal3_start",50);  rospy.set_param("goal3_end",80);    rospy.set_param("goal3_expect",77)

    #  obstacles_postion
    rospy.set_param("obs_count",3)

    rospy.set_param("obs1_x",3);    rospy.set_param("obs1_y",2.5);  rospy.set_param("obs1_r",0.375)
    rospy.set_param("obs1_vx",0);   rospy.set_param("obs1_vy",0)

    rospy.set_param("obs2_x",1);    rospy.set_param("obs2_y",4);    rospy.set_param("obs2_r",0.25)
    rospy.set_param("obs2_vx",0);   rospy.set_param("obs2_vy",0)

    rospy.set_param("obs3_x",2);    rospy.set_param("obs3_y",1);    rospy.set_param("obs3_r",0.5)
    rospy.set_param("obs3_vx",0);   rospy.set_param("obs3_vy",0)

    #  else params
    rospy.set_param("dist_goal",0.2)
    rospy.set_param("dist_obs",0.15)

    rospy.loginfo("All params are loaded !")