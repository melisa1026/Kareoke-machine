using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Script1 : MonoBehaviour
{
    private bool jumpKeyWasPressed;
    private float horizontalInput;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
       if (Input.GetKeyDown(KeyCode.Space))
        {
         jumpKeyWasPressed = true;
        }

        horizontalInput = Input.GetAxis("Horizontal");
    }

    //Fixed Update is called once every physics update
    private void FixedUpdate() 
    {
         if (jumpKeyWasPressed)
        {
         GetComponent<Rigidbody>().AddForce(Vector3.up*5, ForceMode.VelocityChange);
         jumpKeyWasPressed = false;
        }

        GetComponent<Rigidbody>().velocity = new Vector3(horizontalInput*3,  GetComponent<Rigidbody>().velocity.y, 0);
    }
}
